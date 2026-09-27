#!/usr/bin/env python3
"""Optional PARS invariant ledger. Python 3.9+, standard library only."""

import argparse
import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import stat
import subprocess
import sys
import tempfile
import time

SOURCES = ("user", "authoritative specification", "derived necessity",
           "safety/containment", "accepted test contract")
STATUSES = ("ACTIVE", "SUPERSEDED", "UNRESOLVED_CONTRACT")
PHASES = ("pre_build", "post_build")
FIELDS = ("ID", "Source", "Predicate", "Scope", "Verifier", "Status", "build_sensitive")


def timestamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def load(path, create=False):
    if not path.exists():
        if create:
            return {"invariants": []}
        raise ValueError("ledger does not exist: " + str(path))
    if not path.is_file():
        raise ValueError("ledger must be a regular JSON file")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as exc:
        raise ValueError("invalid ledger JSON: " + str(exc)) from exc
    if not isinstance(data, dict) or not isinstance(data.get("invariants"), list):
        raise ValueError("invalid ledger: expected an invariants list")
    ids = set()
    for inv in data["invariants"]:
        if not isinstance(inv, dict):
            raise ValueError("invalid ledger: invariant must be an object")
        for field in ("ID", "Source", "Predicate", "Verifier", "Status"):
            if not isinstance(inv.get(field), str):
                raise ValueError("invalid ledger: missing or invalid " + field)
        if (not inv["ID"].strip() or not inv["Predicate"].strip()
                or inv["ID"] in ids or inv["Source"] not in SOURCES
                or inv["Status"] not in STATUSES
                or not isinstance(inv.get("Scope"), list)
                or any(not isinstance(s, str) or not s.strip() for s in inv["Scope"])
                or not isinstance(inv.get("build_sensitive"), bool)
                or not isinstance(inv.get("replays"), list)
                or any(not isinstance(r, dict) for r in inv["replays"])
                or not isinstance(inv.get("history"), list)):
            raise ValueError("invalid ledger: malformed or duplicate invariant")
        ids.add(inv["ID"])
    return data


def save(path, data):
    """Replace only after the complete new JSON has been written."""
    fd, name = tempfile.mkstemp(prefix=".pars-ledger-", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(data, stream, indent=2, ensure_ascii=False, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def contract(inv):
    text = json.dumps({key: inv[key] for key in FIELDS}, sort_keys=True)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def scope_state(inv, base):
    """Capture literal paths and directory descendants, excluding .git."""
    state = {}

    def record(path):
        info = path.stat()
        if path.is_symlink() and stat.S_ISDIR(info.st_mode):
            raise ValueError("scope directory symlinks are unsupported: " + str(path))
        if stat.S_ISDIR(info.st_mode):
            state[str(path)] = ["directory"]
        elif stat.S_ISREG(info.st_mode):
            digest = hashlib.sha256()
            with path.open("rb") as stream:
                for chunk in iter(lambda: stream.read(65536), b""):
                    digest.update(chunk)
            state[str(path)] = ["file", digest.hexdigest(), stat.S_IMODE(info.st_mode),
                                os.readlink(path) if path.is_symlink() else None]
        else:
            raise ValueError("scope must contain regular files or directories: " + str(path))

    def walk_error(exc):
        raise exc

    for raw in inv["Scope"]:
        path = Path(raw).expanduser()
        if not path.is_absolute():
            path = base / path
        record(path)
        if path.is_dir():
            for root, directories, files in os.walk(path, onerror=walk_error):
                directories[:] = sorted(d for d in directories if d != ".git")
                for name in directories + sorted(files):
                    record(Path(root) / name)
    return state


def verdict(inv, phase, base):
    if inv["Status"] == "SUPERSEDED":
        return "SUPERSEDED"
    if inv["Status"] == "UNRESOLVED_CONTRACT":
        return "INCONSISTENT_CONTRACT"
    if not inv["Verifier"].strip() or inv["Verifier"].startswith("MANUAL:"):
        return "UNVERIFIABLE"
    records = [r for r in inv["replays"] if r.get("phase") == phase]
    if not records:
        return "NEVER_REPLAYED"
    record = records[-1]
    if record.get("result") == "FAIL":
        return "FAILED"
    if record.get("result") != "PASS":
        return "UNVERIFIABLE"
    if record.get("contract") != contract(inv):
        return "STALE"
    if not isinstance(record.get("time_ns"), int) or record["time_ns"] <= 0:
        return "UNVERIFIABLE"
    try:
        current = scope_state(inv, base)
    except (OSError, ValueError):
        return "UNVERIFIABLE"
    if current != record.get("scope"):
        return "STALE"
    return "SATISFIED"


def applicable(inv, phase):
    return inv["Status"] == "ACTIVE" and (phase == "pre_build" or inv["build_sensitive"])


def outcome(data, phase, base):
    if any(i["Status"] == "UNRESOLVED_CONTRACT" for i in data["invariants"]):
        return "INCONSISTENT_CONTRACT"
    results = [verdict(i, phase, base) for i in data["invariants"] if applicable(i, phase)]
    if "FAILED" in results:
        return "INVALID_FINAL_STATE" if phase == "pre_build" else "INVALID_BUILT_ARTIFACT"
    if any(result != "SATISFIED" for result in results):
        return "UNVERIFIABLE"
    return "PASS"


def run_verifier(command, base, timeout):
    if not command.strip() or command.startswith("MANUAL:"):
        return "UNVERIFIABLE", "manual or missing verifier"
    # A file avoids retaining unbounded command output in memory or waiting on
    # pipes inherited by a verifier's children. Keep only a bounded receipt.
    with tempfile.TemporaryFile() as output:
        try:
            process = subprocess.Popen(command, shell=True, cwd=base,
                                       stdin=subprocess.DEVNULL, stdout=output,
                                       stderr=subprocess.STDOUT, start_new_session=(os.name == "posix"))
            try:
                code = process.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                if os.name == "posix":
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                else:
                    process.kill()
                process.wait()
                return "UNVERIFIABLE", "verifier timed out after " + str(timeout) + " seconds"
        except OSError as exc:
            return "UNVERIFIABLE", "verifier could not run: " + str(exc)
        output.seek(0)
        evidence = output.read(4096).decode("utf-8", errors="replace")
        return ("PASS" if code == 0 else "FAIL"), "exit=" + str(code) + " " + evidence


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--ledger", default="./pars-ledger.json", type=Path)
    commands = result.add_subparsers(dest="command", required=True)
    freeze = commands.add_parser("freeze", help="record an invariant")
    freeze.add_argument("--id", required=True)
    freeze.add_argument("--source", choices=SOURCES, default="user")
    freeze.add_argument("--predicate", required=True)
    freeze.add_argument("--scope", action="append", default=[])
    freeze.add_argument("--verifier", default="")
    freeze.add_argument("--build-sensitive", action="store_true")
    freeze.add_argument("--status", choices=STATUSES, default="ACTIVE")
    replay = commands.add_parser("replay", help="explicitly execute stored verifiers")
    replay.add_argument("--phase", choices=PHASES, required=True)
    replay.add_argument("--timeout", type=float, default=120.0, help="seconds per verifier (default: 120)")
    status = commands.add_parser("status", help="inspect recorded evidence without executing it")
    status.add_argument("--phase", choices=PHASES, default="pre_build")
    gate = commands.add_parser("gate", help="evaluate recorded evidence without executing it")
    gate.add_argument("--phase", choices=PHASES, required=True)
    supersede = commands.add_parser("supersede", help="retire an invariant without erasing history")
    supersede.add_argument("--id", required=True)
    supersede.add_argument("--reason", required=True)
    return result


def main(argv=None):
    args = parser().parse_args(argv)
    path = args.ledger.absolute()
    try:
        data = load(path, create=args.command == "freeze")
        if args.command == "freeze":
            if not args.id.strip() or not args.predicate.strip() or any(not s.strip() for s in args.scope):
                raise ValueError("ID, Predicate, and each Scope must be nonempty")
            if any(i["ID"] == args.id for i in data["invariants"]):
                raise ValueError("invariant ID already exists: " + args.id)
            data["invariants"].append({
                "ID": args.id, "Source": args.source, "Predicate": args.predicate,
                "Scope": args.scope, "Verifier": args.verifier, "Status": args.status,
                "build_sensitive": args.build_sensitive, "created": timestamp(),
                "replays": [], "history": [],
            })
            save(path, data)
            print(args.id + " " + args.status)
        elif args.command == "supersede":
            if not args.reason.strip():
                raise ValueError("supersede requires a nonempty reason")
            inv = next((i for i in data["invariants"] if i["ID"] == args.id), None)
            if inv is None:
                raise ValueError("unknown invariant ID: " + args.id)
            inv["history"].append({"time": timestamp(), "from": inv["Status"],
                                   "to": "SUPERSEDED", "reason": args.reason})
            inv["Status"] = "SUPERSEDED"
            save(path, data)
            print(args.id + " SUPERSEDED")
        elif args.command == "replay":
            if not math.isfinite(args.timeout) or args.timeout <= 0:
                raise ValueError("timeout must be a finite positive number")
            for inv in data["invariants"]:
                if not applicable(inv, args.phase):
                    continue
                record = {"phase": args.phase, "time": timestamp(), "time_ns": time.time_ns(),
                          "contract": contract(inv)}
                try:
                    record["scope"] = scope_state(inv, path.parent)
                    result, evidence = run_verifier(inv["Verifier"], path.parent, args.timeout)
                except (OSError, ValueError) as exc:
                    result, evidence = "UNVERIFIABLE", "scope unavailable: " + str(exc)
                record.update(result=result, evidence=evidence, completed=timestamp())
                inv["replays"].append(record)
                print(inv["ID"] + " " + result + " " + evidence.strip())
            save(path, data)
            return 0 if outcome(data, args.phase, path.parent) == "PASS" else 1
        elif args.command == "status":
            for inv in data["invariants"]:
                print(inv["ID"] + " [" + inv["Status"] + "] " + verdict(inv, args.phase, path.parent))
        elif args.command == "gate":
            result = outcome(data, args.phase, path.parent)
            print(result)
            return 0 if result == "PASS" else 1
        return 0
    except (OSError, ValueError) as exc:
        print("pars-ledger: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
