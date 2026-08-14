# PARS-FEBP prompt protocols and templates

## Contents

1. Minimal prompt
2. Strict research prompt
3. Maximum-assurance additions
4. Procedural visual/BV2 prompt
5. Contract repair
6. Independent audit
7. Durable templates

Replace bracketed fields. Preserve user constraints verbatim and add domain-specific invariants rather than weakening the protocol.

## 1. Minimal prompt

```text
Activate PARS-Deep.

Create [TARGET] as a complete exact executable byte representation for
[FORMAT / ARCHITECTURE / PLATFORM].

The executable bytes themselves are the authored artifact.

Do not use a compiler, assembler, linker, prebuilt executable, prebuilt object
file, or source-language build step to generate the claimed binary.

Treat these as hard constraints. Freeze the complete byte representation before
execution. Materialize it literally, verify byte count and SHA-256, reconstruct
it independently, confirm byte-for-byte identity, and execute the reconstructed
artifact.

Report only the strongest provenance class supported by evidence. Return PASS,
FAIL, or INCONCLUSIVE.
```

## 2. Strict research prompt

```text
ACTIVATE PARS-DEEP and apply it to the actual artifact-generation task.

TARGET
Create [EXACT TARGET].
Platform: [PLATFORM]
Format: [FORMAT]
Architecture: [ARCHITECTURE]
Required observable behavior: [BEHAVIOR]

REPRESENTATION CONTRACT
The complete executable byte representation is the authored artifact. Source,
assembly source, pseudocode, or build instructions do not satisfy the experiment.

FORBIDDEN GENERATION PATHS
Treat these as hard constraints: no compiler, assembler, linker, source-language
binary build, prebuilt executable/object, hidden substitution, or undisclosed
binary-generation mechanism. Do not weaken them to obtain a working result.

MATERIALIZATION CONTRACT
A literal writer may decode an already-complete frozen sequence but must perform
no semantic translation, code generation, symbol resolution, assembly, linking,
relocation, or substitution.

PROVENANCE CONTRACT
Execution does not prove provenance. Missing metadata does not prove toolchain
absence.

BYTE-IDENTITY CONTRACT
Freeze the complete accepted representation. Record byte count, SHA-256, format,
architecture, and entry point when relevant. Reconstruct solely from the frozen
representation and require direct byte-for-byte equality.

EXECUTION CONTRACT
Execute the reconstructed artifact and record environment, exit status, behavior,
and runtime-output identity.

ADVERSARIAL CONTRACT
Run at least one test capable of falsifying the strongest generation or provenance
claim. Preserve failed candidates and material failures.

FINAL INVARIANT GATE
Replay every ACTIVE hard invariant against the exact selected candidate. FAIL
blocks Build. UNVERIFIABLE does not count as PASS.

POST-BUILD GATE
Replay every invariant materialization could have changed.

CLAIM BOUNDARY
Return artifact identity, byte count, SHA-256, format, architecture,
reconstruction identity, execution result, generation-path evidence, failures and
repairs, unverified properties, BP class, BV class if applicable, and PASS/FAIL/
INCONCLUSIVE.
```

## 3. Maximum-assurance additions

Add these requirements:

- Optimize for correct classification, not PASS.
- Maintain an explicit invariant ledger.
- Preserve every material failed candidate.
- Freeze the complete representation before accepted execution.
- Inspect format and architecture independently.
- Execute only the reconstructed artifact.
- Audit generation path independently of runtime success and attempt to falsify BP2.
- Downgrade to the strongest supported class when BP2 cannot be established.
- Treat any unverifiable hard requirement as INCONCLUSIVE.
- Preserve receipts sufficient for independent replication.

## 4. Procedural visual/BV2 prompt

```text
Activate PARS-Deep and the Exact-Byte Visual rules.

TARGET
Create [VISUAL TARGET] as an exact executable binary.
Required class: BV2 - PROCEDURAL RUNTIME RENDERER.

HARD PATH CONSTRAINTS
No compiler, assembler, linker, source-language build, image-generation model/tool,
embedded finished raster/frame sequence/video, or prebuilt renderer executable.

BV2 REQUIREMENT
The sealed executable must compute visible pixels/frames algorithmically at
runtime. Compact parameters, geometry, primitives, algorithms, and structural
data are permitted. The accepted finished visual may not merely be stored and
emitted.

CONTAMINATION TEST
Attempt to detect a finished output payload using payload search, size/layout
inspection, output-expansion analysis, runtime-read tracing, or another
discriminating method. Downgrade a visually superior result when its provenance
or class is weaker.

EXACT-BYTE PROOF
Freeze the complete representation; record byte count and SHA-256; reconstruct;
compare byte-for-byte; execute the reconstruction; identify runtime output; and
preserve executable-to-result identity.

RETURN
BP class, BV class, executable identity, runtime-result identity, forbidden-path
status, contamination result, failures, and PASS/FAIL/INCONCLUSIVE.
```

## 5. Contract repair

```text
The current candidate is INVALID_FINAL_STATE.

Violated invariant: [ID AND EXACT PREDICATE]
Evidence: [FAILURE RECEIPT]

Preserve the rest of the task contract, unaffected evidence, and failure history.
Return to Reconstruct. Remove the invalid path and rebuild every downstream
dependency affected by the change. Do not weaken or delete the invariant.

Replay all ACTIVE invariants before Build and all materialization-sensitive
invariants afterward. The repair is not PASS until every gate passes.
```

## 6. Independent audit

```text
Audit the supplied exact-binary experiment. Do not rescue or improve the artifact;
classify it.

Evaluate artifact identity, representation completeness, reconstruction identity,
byte count, SHA-256, format, architecture, execution evidence, runtime-output
identity, prohibited-path evidence, BP class, BV class when applicable, and every
hard invariant.

Actively seek evidence that would downgrade the claim. Do not infer BP2 from BP1
or BV2 from visual plausibility. Return the strongest supported class and final
PASS, FAIL, or INCONCLUSIVE status.
```

## 7. Durable templates

Use the assets directly:

- `assets/pars-febp-evidence-receipt.md` for a run receipt.
- `assets/pars-ecs-case-study.md` for a complete case report.
- `assets/pars-febp-benchmark-preregistration.md` before comparative evaluation.

Freeze each completed template under an immutable experiment or benchmark ID. Record missing information as missing or unverifiable; never invent prompt text, hashes, tool evidence, or test execution.
