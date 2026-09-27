# PARS invariant ledger

An optional helper for recording and replaying the hard invariants in [architecture and execution, section 4](../../references/architecture-and-execution.md#4-hard-invariant-system). The skill does not require it. The CLI uses Python 3.9 or later and only the standard library.

The JSON ledger stores `ID`, `Source`, `Predicate`, `Scope`, `Verifier`, and `Status`, together with replay receipts and supersession history. `Source` accepts `user`, `authoritative specification`, `derived necessity`, `safety/containment`, or `accepted test contract`; its default is `user`. `Status` accepts `ACTIVE`, `SUPERSEDED`, or `UNRESOLVED_CONTRACT`; its default is `ACTIVE`.

## Worked example

Run from the repository root in a POSIX shell. This example checks only that `README.md` exists, not that its contents satisfy a specification. Freeze predicates and verifiers that cover the actual acceptance criteria.

```bash
python3 tools/pars-ledger/pars_ledger.py freeze --id readme-present --source user --predicate "The built repository contains README.md" --scope README.md --verifier 'python3 -c "from pathlib import Path; assert Path(\"README.md\").is_file()"' --build-sensitive
python3 tools/pars-ledger/pars_ledger.py status
python3 tools/pars-ledger/pars_ledger.py replay --phase pre_build
python3 tools/pars-ledger/pars_ledger.py gate --phase pre_build
```

The initial status is `NEVER_REPLAYED`. Replay runs the verifier and records its result, time, bounded output, and scope content digests. A successful gate prints `PASS` and exits zero. Only then may Build begin.

After materializing the artifact, replay the invariants marked `--build-sensitive`:

```bash
python3 tools/pars-ledger/pars_ledger.py replay --phase post_build
python3 tools/pars-ledger/pars_ledger.py gate --phase post_build
python3 tools/pars-ledger/pars_ledger.py status --phase post_build
```

Pre-Build and post-Build receipts are separate. The pre-Build gate considers every `ACTIVE` invariant; the post-Build gate considers `ACTIVE` invariants marked `--build-sensitive`. `UNRESOLVED_CONTRACT` blocks both phases. Mark every predicate that materialization could change as build-sensitive. Replay after each build: this helper observes scope changes, not build invocations.

To retire a requirement, preserve its record and give the reason:

```bash
python3 tools/pars-ledger/pars_ledger.py supersede --id readme-present --reason "Replaced by a more specific artifact requirement"
```

## Storage and replay

The default ledger is `./pars-ledger.json`. Supply `--ledger PATH` before the command to select another file. Its parent directory must exist. Relative scope paths and verifier working directories are relative to the ledger's parent directory, so changing the caller's working directory does not change what a stored relative scope means.

Repeat `--scope` for multiple literal files or directories. Directory scopes include descendants, except `.git`; directory symlinks and special files are unsupported. Keep the ledger outside its own declared scope. SHA-256 content digests, file permissions, symlink targets, and directory membership detect changes after a pass, including changes during replay. Missing or unreadable scope paths are `UNVERIFIABLE`. An omitted scope permits command-only checks but provides no artifact staleness detection. The ledger is not protection against deliberate tampering.

Replay has a 120-second timeout per verifier; `replay --timeout SECONDS` changes it. A shell exit code of zero records `PASS`; any other exit records `FAIL`. Timeout, execution errors, missing verifiers, and `MANUAL:<how>` verifiers record `UNVERIFIABLE`. Manual checks remain blocking: this helper has no command for asserting that a manual check passed.

Writes use a temporary file followed by atomic replacement. Run one writer at a time; atomic replacement does not provide concurrent edit merging. Replay appends receipts, and supersession retains prior failures and the retirement reason. Corrupt or malformed ledgers produce a clear error without overwriting the file. A missing ledger also blocks the gate. An existing ledger with no applicable invariants passes; this does not establish that all necessary requirements were frozen.

## Status and gate outcomes

`status` reports every invariant for the selected phase and does not run verifiers. It defaults to `pre_build`; its successful exit means inspection completed, not that the gate passed.

| Status verdict | Meaning | Gate outcome |
| --- | --- | --- |
| `SATISFIED` | The latest receipt for this phase passed and its scope is current. | `PASS` when every applicable invariant is satisfied. |
| `NEVER_REPLAYED` | No receipt exists for this phase. | `UNVERIFIABLE` |
| `STALE` | The scope changed after the pass, comparing SHA-256 content digests of every file in scope, file permissions, symlink targets, directory membership, and the invariant's own contract digest. | `UNVERIFIABLE` |
| `FAILED` | The latest verifier exited nonzero. | `INVALID_FINAL_STATE` before Build; `INVALID_BUILT_ARTIFACT` after Build. |
| `UNVERIFIABLE` | A manual check, missing evidence, unavailable scope, or execution problem prevents verification. | `UNVERIFIABLE` |
| `INCONSISTENT_CONTRACT` | An invariant has status `UNRESOLVED_CONTRACT`. | `INCONSISTENT_CONTRACT` |
| `SUPERSEDED` | The requirement was retired and its history remains. | Excluded from the gate. |

Contract conflicts take precedence over verifier failures; failures take precedence over missing evidence. `gate` is read-only and exits zero only for `PASS`. Blocking gates and unsuccessful replays exit 1; invalid input or unreadable ledgers exit 2. The helper records declared conflicts; it does not infer contradictions between natural-language predicates.

## Security

Verifiers are shell commands stored in the ledger and run on replay. Run only ledgers you trust. Commands inherit the caller's permissions and environment; this helper is not a sandbox. Review commands before replay and avoid secrets in command text or output, since replay receipts retain up to 4096 bytes of combined output. On POSIX systems a timeout kills the verifier's process group; on other systems it kills the immediate shell process and may leave descendants running. A timeout is not containment.

## Tests

From the repository root:

```bash
python3 -m unittest discover -s tools/pars-ledger/tests
```

The tests exercise successful gates and blocking cases, including failures, manual checks, stale scopes, unresolved contracts, phase isolation, timeouts, supersession, and corrupt JSON preservation.
