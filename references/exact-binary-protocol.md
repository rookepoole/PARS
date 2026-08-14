# Exact-binary generation, provenance, and verification

## Contents

1. Activation and operational definition
2. Experimental planes
3. Provenance and visual classes
4. Eleven prompt locks
5. Exact-byte proof chain
6. Containment and repair
7. Acceptance and reporting

## 1. Activation and operational definition

Activate this module only when the task concerns direct binary generation, exact executable-byte representation, provenance, opaque-binary analysis, contained execution, binary repair, or a visual whose claimed generation path is an exact executable byte stream.

Use this operational definition:

> A freehand exact binary is a machine-consumable artifact whose complete byte-level representation is authored directly under a frozen generation contract, with claimed prohibited generation mechanisms excluded from the audited path, and whose published representation losslessly reconstructs the accepted artifact.

Do not treat this as an externally standardized definition.

## 2. Experimental planes

Separate three functional planes:

- Generation/Reasoning Plane: decide artifact semantics and every byte under the frozen contract.
- Materialization Plane: convert an already-complete representation into literal bytes without adding executable information.
- Evidence Plane: hash, compare, inspect, execute, capture, and audit the artifact.

Classify tools by information contribution, not name. A step is literal materialization only when another correct decoder would produce the same bytes because all output bytes were already determined.

Literal operations may include hex-pair decoding, Base64 decoding, escaped-byte conversion, and predetermined chunk concatenation. Semantic generation includes mnemonic-to-opcode translation, label displacement calculation, symbol resolution, generated executable headers, relocation, and linking.

Freeze the complete accepted representation before materialization. Any post-freeze byte change creates a new candidate revision and leaves the prior candidate in failure history.

## 3. Provenance and visual classes

### Binary provenance

- `BP0`: exact artifact identity is established.
- `BP1`: the frozen recorded representation reconstructs the exact artifact.
- `BP2`: the audited path supports the stated absence of conventional compiler/assembler/linker participation in the claimed creation/materialization path.
- `BP3`: creation provenance is unknown or inadequately evidenced.

BP1 does not imply BP2. Missing toolchain metadata does not prove BP2. A prompt prohibition is an obligation, not evidence of compliance.

### Binary visuals

- `BV0`: exact-byte emitter containing a finished raster/video payload or equivalent finished output.
- `BV1`: binary-first raster builder that first materializes the final raster at runtime from compact structural data or primitives.
- `BV2`: procedural runtime renderer that computes visible pixels/frames algorithmically and contains no finished output payload.
- `BV3`: reference-conditioned BV1 or BV2 reconstruction with separately frozen reference identity and rights state.

Do not promote BV0 to BV1/BV2/BV3. When "binary first" is required, accept only BV1, BV2, or BV3 unless the user explicitly accepts a downgraded emitter claim.

Distinguish generation dependencies, runtime dependencies, and evidence dependencies. An operating system, host, display server, graphics driver, or WebAssembly runtime may be required for execution without becoming a generator.

## 4. Eleven prompt locks

Use the whitepaper-defined PARS-FEBP locks in order:

1. Activation: apply PARS to the task; prevent explanation-only substitution.
2. Objective: freeze platform, format, architecture, behavior, inputs, outputs, and termination.
3. Representation: make the complete byte representation the authored artifact.
4. Negative Path: prohibit every disallowed generator, toolchain, prebuilt object, and substitution path.
5. Invariant: treat acceptance conditions as hard predicates.
6. Provenance: separate runtime success from creation-path evidence.
7. Reconstruction: require the disclosed representation to rebuild the accepted artifact.
8. Execution: run the reconstructed artifact, not a development copy.
9. Evidence: require objective receipts.
10. Adversarial: attempt to falsify the strongest claim.
11. Claim Boundary: report only the strongest supported class.

Optimize for correct `PASS`, `FAIL`, or `INCONCLUSIVE` classification, not for obtaining PASS.

## 5. Exact-byte proof chain

Run the full chain when applicable:

1. Freeze task contract.
2. Author the complete byte representation.
3. Freeze representation identity.
4. Replay all final invariants.
5. Materialize literally.
6. Replay materialization-sensitive invariants.
7. Record byte count and SHA-256.
8. Audit format, architecture, entry point, and required structure.
9. Reconstruct independently from the same frozen representation.
10. Require equal length and direct byte-for-byte identity.
11. Audit the generation path.
12. Execute the reconstructed artifact under containment.
13. Verify runtime result identity and behavior.
14. Run a hostile contamination/provenance test.
15. Assign BP and, when applicable, BV class.
16. Return `PASS`, `FAIL`, or `INCONCLUSIVE`.

Treat direct byte comparison as the primary equality predicate; use SHA-256 as a compact identity receipt. Preserve executable and runtime-output identities separately.

For BV1/BV2/BV3, test for disguised or compressed finished output using payload search, size/layout inspection, output-expansion analysis, runtime-read tracing, or direct structural inspection. Output expansion alone is supporting evidence, not proof.

For a public showcase, order evidence as:

`SOURCE/REFERENCE -> RIGHTS/PROVENANCE LOCK -> TARGET CONTRACT -> COMPLETE BYTE STREAM -> RECONSTRUCTION -> BYTE COUNT/HASH/FORMAT -> EXECUTION -> RUNTIME RESULT -> POST-RUNTIME IDENTITY -> RESULTS`

Require a dedicated RESULTS segment stating BP/BV class, artifact identity, runtime-result identity, relevant rights state, and final status. Disclose stitched evidence and separate capture infrastructure from generation.

## 6. Containment and repair

Before executing an unknown or newly generated binary:

- inspect statically;
- use a disposable, non-root, credential-free environment;
- deny outbound network by default;
- apply resource limits and deterministic inputs/environment;
- fail closed when authorization or containment is unresolved.

For exact repair:

1. Freeze original identity.
2. Separate intended from observed behavior.
3. Diagnose before trial patching when feasible.
4. Choose the smallest supported patch.
5. Preserve exact offsets, original bytes, and replacement bytes.
6. Predict behavior before applying the patch.
7. Reject undeclared changes.
8. Reconstruct affected offsets, layout, branches, headers, and dependencies.
9. Rerun positive, unaffected, negative, identity, provenance, and post-Build tests.

Never execute an unknown binary directly on a normal host merely because the user requested analysis.

## 7. Acceptance and reporting

A visually convincing or successfully executing artifact is insufficient. PASS requires the exact requested behavior, identity, reconstruction, provenance, path constraints, and BP/BV class to be established.

Report at minimum:

- artifact and frozen-representation identities;
- byte count and SHA-256;
- format, architecture, and entry point where relevant;
- materializer and its functional role;
- direct reconstruction comparison;
- execution environment, exit status, and observed behavior;
- runtime-output identity;
- generation-path evidence and hostile-test result;
- preserved failures and repairs;
- BP/BV class;
- unverifiable properties;
- `PASS`, `FAIL`, or `INCONCLUSIVE`.

If upstream byte-stream creation provenance is missing, retain BP1 when supported but do not promote to BP2. Obtain upstream evidence or weaken the claim.
