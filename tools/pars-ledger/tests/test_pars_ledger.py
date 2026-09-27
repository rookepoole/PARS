"""Exercise the CLI, including failing gates, against isolated ledgers."""

import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
SCRIPT = Path(__file__).resolve().parents[1] / "pars_ledger.py"


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name)
        self.ledger = self.root / "ledger.json"

    def cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), "--ledger", str(self.ledger), *args],
                              cwd=self.root, capture_output=True, text=True, timeout=10)

    def freeze(self, ident="a", verifier="exit 0", *extra):
        result = self.cli("freeze", "--id", ident, "--predicate", "p", "--verifier", verifier, *extra)
        self.assertEqual(result.returncode, 0, result.stderr)

    def gate(self, phase, expected, passes=False):
        result = self.cli("gate", "--phase", phase)
        if passes:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), expected)

    def test_freeze_then_status_never_replayed(self):
        self.freeze()
        self.assertIn("NEVER_REPLAYED", self.cli("status").stdout)
        self.gate("pre_build", "UNVERIFIABLE")

    def test_pass_verifier_satisfied_and_gate(self):
        self.freeze()
        self.gate("pre_build", "UNVERIFIABLE")
        self.assertEqual(self.cli("replay", "--phase", "pre_build").returncode, 0)
        self.assertIn("SATISFIED", self.cli("status").stdout)
        self.gate("pre_build", "PASS", passes=True)

    def test_failed_verifier_invalid_final_state(self):
        self.freeze("a", "exit 1")
        self.assertNotEqual(self.cli("replay", "--phase", "pre_build").returncode, 0)
        self.assertIn("FAILED", self.cli("status").stdout)
        self.gate("pre_build", "INVALID_FINAL_STATE")

    def test_manual_verifier_unverifiable(self):
        self.freeze("m", "MANUAL:inspect the file")
        self.assertIn("UNVERIFIABLE", self.cli("status").stdout)
        self.gate("pre_build", "UNVERIFIABLE")
        self.assertNotEqual(self.cli("replay", "--phase", "pre_build").returncode, 0)
        self.gate("pre_build", "UNVERIFIABLE")

    def test_scope_byte_change_is_stale(self):
        scoped = self.root / "f.txt"
        scoped.write_text("original", encoding="utf-8")
        self.freeze("s", "exit 0", "--scope", "f.txt")
        self.assertEqual(self.cli("replay", "--phase", "pre_build").returncode, 0)
        self.gate("pre_build", "PASS", passes=True)
        scoped.write_text("changed", encoding="utf-8")
        self.assertIn("STALE", self.cli("status").stdout)
        self.gate("pre_build", "UNVERIFIABLE")

    def test_scope_touch_with_identical_bytes_stays_satisfied(self):
        scoped = self.root / "f.txt"
        scoped.write_text("original", encoding="utf-8")
        self.freeze("s", "exit 0", "--scope", "f.txt")
        self.assertEqual(self.cli("replay", "--phase", "pre_build").returncode, 0)
        self.gate("pre_build", "PASS", passes=True)
        os.utime(scoped, None)
        self.assertIn("SATISFIED", self.cli("status").stdout)
        self.gate("pre_build", "PASS", passes=True)
        record = json.loads(self.ledger.read_text())["invariants"][0]["replays"][-1]
        newer = record["time_ns"] + 1000000000
        os.utime(scoped, ns=(newer, newer))
        self.assertIn("SATISFIED", self.cli("status").stdout)
        self.gate("pre_build", "PASS", passes=True)

    def test_scope_byte_change_with_restored_mtime_is_stale(self):
        scoped = self.root / "f.txt"
        scoped.write_text("original", encoding="utf-8")
        self.freeze("s", "exit 0", "--scope", "f.txt")
        self.assertEqual(self.cli("replay", "--phase", "pre_build").returncode, 0)
        self.gate("pre_build", "PASS", passes=True)
        original = scoped.stat()
        scoped.write_text("modified", encoding="utf-8")
        os.utime(scoped, ns=(original.st_atime_ns, original.st_mtime_ns))
        self.assertEqual(scoped.stat().st_mtime_ns, original.st_mtime_ns)
        self.assertIn("STALE", self.cli("status").stdout)
        self.gate("pre_build", "UNVERIFIABLE")

    def test_new_file_in_scoped_directory_is_stale(self):
        directory = self.root / "d"
        directory.mkdir()
        self.freeze("s", "exit 0", "--scope", "d")
        self.assertEqual(self.cli("replay", "--phase", "pre_build").returncode, 0)
        self.gate("pre_build", "PASS", passes=True)
        (directory / "new.txt").write_text("new", encoding="utf-8")
        self.assertIn("STALE", self.cli("status").stdout)
        self.gate("pre_build", "UNVERIFIABLE")

    def test_unresolved_contract_blocks_both_phases(self):
        result = self.cli("freeze", "--id", "c", "--predicate", "p", "--status", "UNRESOLVED_CONTRACT")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("INCONSISTENT_CONTRACT", self.cli("status").stdout)
        for phase in ("pre_build", "post_build"):
            self.gate(phase, "INCONSISTENT_CONTRACT")

    def test_post_build_failure_invalid_built_artifact(self):
        self.freeze("b", "exit 1", "--build-sensitive")
        self.assertNotEqual(self.cli("replay", "--phase", "post_build").returncode, 0)
        self.gate("post_build", "INVALID_BUILT_ARTIFACT")

    def test_supersede_keeps_history_and_removes_blocker(self):
        self.freeze("a", "exit 1")
        self.cli("replay", "--phase", "pre_build")
        self.gate("pre_build", "INVALID_FINAL_STATE")
        result = self.cli("supersede", "--id", "a", "--reason", "requirement replaced")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.gate("pre_build", "PASS", passes=True)
        inv = json.loads(self.ledger.read_text())["invariants"][0]
        self.assertEqual(inv["Status"], "SUPERSEDED")
        self.assertEqual(inv["replays"][0]["result"], "FAIL")
        self.assertEqual(inv["history"][0]["reason"], "requirement replaced")

    def test_corrupt_json_preserved_by_all_commands(self):
        original = b"{not json"
        self.ledger.write_bytes(original)
        commands = [
            ("freeze", "--id", "a", "--predicate", "p"), ("status",),
            ("replay", "--phase", "pre_build"), ("gate", "--phase", "pre_build"),
            ("supersede", "--id", "a", "--reason", "replacement"),
        ]
        for command in commands:
            with self.subTest(command=command):
                result = self.cli(*command)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("invalid ledger JSON", result.stderr)
                self.assertEqual(self.ledger.read_bytes(), original)

    def test_phase_receipts_do_not_substitute_for_each_other(self):
        self.freeze("a", "exit 0", "--build-sensitive")
        self.cli("replay", "--phase", "pre_build")
        self.gate("post_build", "UNVERIFIABLE")
        self.cli("replay", "--phase", "post_build")
        self.gate("post_build", "PASS", passes=True)
        self.freeze("b", "exit 0", "--build-sensitive")
        self.cli("replay", "--phase", "post_build")
        self.gate("pre_build", "UNVERIFIABLE")

    def test_post_build_selects_build_sensitive_only(self):
        self.freeze("a", "exit 1")
        self.freeze("b", "exit 0", "--build-sensitive")
        self.gate("post_build", "UNVERIFIABLE")
        self.assertEqual(self.cli("replay", "--phase", "post_build").returncode, 0)
        self.gate("post_build", "PASS", passes=True)
        records = json.loads(self.ledger.read_text())["invariants"]
        self.assertEqual(records[0]["replays"], [])

    def test_missing_scope_blocks(self):
        self.freeze("s", "exit 0", "--scope", "missing.txt")
        self.assertNotEqual(self.cli("replay", "--phase", "pre_build").returncode, 0)
        self.assertIn("UNVERIFIABLE", self.cli("status").stdout)
        self.gate("pre_build", "UNVERIFIABLE")

    def test_deleted_scope_blocks(self):
        scoped = self.root / "f.txt"
        scoped.write_text("original", encoding="utf-8")
        self.freeze("s", "exit 0", "--scope", "f.txt")
        self.cli("replay", "--phase", "pre_build")
        self.gate("pre_build", "PASS", passes=True)
        scoped.unlink()
        self.gate("pre_build", "UNVERIFIABLE")

    def test_directory_descendant_change_blocks(self):
        directory = self.root / "artifact" / "nested"
        directory.mkdir(parents=True)
        scoped = directory / "f.txt"
        scoped.write_text("original", encoding="utf-8")
        self.freeze("s", "exit 0", "--scope", "artifact")
        self.cli("replay", "--phase", "pre_build")
        self.gate("pre_build", "PASS", passes=True)
        scoped.write_text("changed", encoding="utf-8")
        self.assertIn("STALE", self.cli("status").stdout)
        self.gate("pre_build", "UNVERIFIABLE")

    @unittest.skipUnless(os.name == "posix", "shell quoting for Python verifier uses POSIX syntax")
    def test_timeout_unverifiable(self):
        command = shlex.quote(sys.executable) + ' -c "import time; time.sleep(10)"'
        self.freeze("t", command)
        result = self.cli("replay", "--phase", "pre_build", "--timeout", "0.05")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("timed out", result.stdout)
        self.gate("pre_build", "UNVERIFIABLE")

    def test_status_and_gate_do_not_run_verifiers(self):
        self.freeze("a", "echo unexpected > marker.txt")
        self.cli("status")
        self.gate("pre_build", "UNVERIFIABLE")
        self.assertFalse((self.root / "marker.txt").exists())

    def test_duplicate_id_preserves_ledger(self):
        self.freeze()
        original = self.ledger.read_bytes()
        result = self.cli("freeze", "--id", "a", "--predicate", "another")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.ledger.read_bytes(), original)

    def test_missing_verifier_blocks(self):
        self.freeze("a", "")
        self.assertIn("UNVERIFIABLE", self.cli("status").stdout)
        self.gate("pre_build", "UNVERIFIABLE")

    def test_missing_ledger_blocks(self):
        result = self.cli("gate", "--phase", "pre_build")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ledger does not exist", result.stderr)
        self.assertFalse(self.ledger.exists())

    def test_invalid_structure_preserves_ledger(self):
        self.ledger.write_text('{"invariants": [42]}', encoding="utf-8")
        original = self.ledger.read_bytes()
        result = self.cli("freeze", "--id", "a", "--predicate", "p")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid ledger", result.stderr)
        self.assertEqual(self.ledger.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
