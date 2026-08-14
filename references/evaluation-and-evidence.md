# Evaluation, evidence packages, and historical cases

## Contents

1. Prospective evaluation question
2. Conditions and cohorts
3. Metrics and classification
4. Failure taxonomy and ablations
5. Historical evidence map
6. Limitations and interpretation
7. Evidence package structure

## 1. Prospective evaluation question

Test the stronger claim rather than assume it:

> Does PARS-FEBP improve correctly verified, constraint-compliant exact-binary generation relative to simpler prompting under a shared model, environment, and resource envelope?

The whitepaper defines this protocol but reports no prospective comparative result.

Preregister hypotheses for constraint compliance, reconstruction reliability, classification accuracy, provenance discipline, and final-invariant protection.

## 2. Conditions and cohorts

Freeze four primary conditions:

- A: naive request with minimal methodology.
- B: explicit exact-binary prompt without full PARS-FEBP.
- C: PARS-FEBP Minimal with core locks, reconstruction, execution, identity, and classification.
- D: PARS-FEBP Strict/Maximum Assurance with explicit invariants, provenance separation, hostile testing, final gate, post-Build replay, and failure preservation.

Hold model, model configuration, tools, environment, task identity, and resource envelope constant within each cohort.

Separate development and held-out cohorts before evaluation. Freeze prompt wording, scoring, verifier implementation, retry policy, exclusions, and promotion rule before revealing held-out outcomes. Do not count development tasks as held-out confirmation.

Use a difficulty ladder from controlled termination through static output, deterministic computation, input-dependent behavior, deterministic file generation, BV1 raster construction, BV2 procedural rendering, and bounded interactive artifacts. Include multiple task families.

## 3. Metrics and classification

Record artifact materialization, structural validity, runtime behavior, exact reconstruction, hard-invariant compliance, provenance classification, visual classification, final status accuracy, repairs, failure preservation, and work cost.

Use the paper-defined composite endpoint `CCEBS` only when all applicable conditions pass:

`structural validity AND required runtime behavior AND complete frozen representation AND exact reconstruction identity AND all hard invariants PASS AND correct claim classification AND required provenance checks AND required post-Build checks`

Add visual-class validity for BV1/BV2 tasks.

Optimize for correct classification:

- `PASS`: every applicable acceptance requirement is established.
- `FAIL`: at least one requirement is demonstrably violated.
- `INCONCLUSIVE`: a required property cannot be established from available evidence.

Use one root attempt plus up to two evidence-triggered repair cycles as the whitepaper's recommended primary design unless a different policy is preregistered. Count an acceptance-relevant artifact or invariant change as a repair, not cosmetic wording.

## 4. Failure taxonomy and ablations

Use the paper-defined F1-F10 taxonomy:

- F1 representation
- F2 executable structure
- F3 instruction
- F4 control flow/offset
- F5 ABI/environment
- F6 behavior
- F7 provenance
- F8 artifact identity
- F9 claim inflation
- F10 evidence capture

Allow multiple codes per run.

Preregister component-removal predictions:

- ABL-1 remove Representation Lock -> more source/assembly substitution.
- ABL-2 remove Negative-Path Lock -> more conventional-toolchain use.
- ABL-3 remove Reconstruction Lock -> more unverifiable or mismatched identity.
- ABL-4 remove Provenance Lock -> more unsupported BP2 claims.
- ABL-5 remove Adversarial Lock -> more hidden contamination.
- ABL-6 remove Final Invariant Gate -> more plausible final candidates violating recognized constraints.
- ABL-7 remove post-Build replay -> more materialization defects delivered.
- ABL-8 remove Reconstruction stage -> more downstream defects after local repair.

Apply severe-regression vetoes for artifact substitution, unsupported BP2, invariant bypass, false reconstruction, or BV0-to-BV2 inflation even if average output success rises.

## 5. Historical evidence map

Treat every case below as Type C historical/development evidence unless prospectively regenerated.

| Case | Artifact | Bytes | SHA-256 / identity | Main contribution | Boundary |
| --- | --- | ---: | --- | --- | --- |
| Starship | ELF64 x86-64 | 907 | `1df35f8ffc64fac0f9e5b9de2c7ad4b763f16d4b40ab7e4e9987b5065030a354` | Compact end-to-end frozen stream, reconstruction, and deterministic PPM output | Original prompt not recovered; historical receipt reported rather than newly recertified |
| LHC Collider v2.1 | ELF64 x86-64 | 2,048 | `04d3da29c36a584baaf9ddd0f8a7e664de1a4da96e2e4292d9cdb4ebcc507b1c` | V1 visual failure, V2 runtime failure, one-byte V2.1 repair, exact reconstruction and runtime replay, recorded BP2/BV2 | Historical provenance classification, not a fresh upstream audit |
| WASM Hyperlattice | WebAssembly v1 | 9,433 | `c1d31cb6f7f052c5053697a1acaa9cb43f2b8ee2959d1df0274f5303bd37e7c3` | Cross-format direct serialization, zero imports, perturbation, regeneration | Supports tested format only, not arbitrary binary generality |
| Binary Brains Gate 9 | ELF64 x86-64 | 34,175 | `a8bd61cc7413bcb0392efa496a1e68f41320c197ce3ef850fd69428f576308cf` | Multiprocess state, one-bit counterfactual, 583/583 checks | Pre-freeze Python arithmetic disclosed; narrow provenance predicate only |
| PARS-VM/4 | ELF64 x86-64 | 5,392 | `5a002c60af45a59c392bffbebbc26d82a6674f0dd7627ee90bbd25089d1908e1` | Custom CPU/ISA/RAM/VGPU, guest-side 3D, reconstruction | Purpose-built VM, not a general x86 PC or modern engine |
| House of the Rising Sun | ELF64 x86-64 | 57,344 | `4d4fe5c98507c4a3bb4f852323bb3ed7dc4ce0612e2873f7b35a2591a4d1ff10` | 210-second runtime, 40,320,044-byte WAV, 112 complete proof pages | Demonstrates proof-scaling burden, not general performance |
| BVIS-001 audit | ELF64 x86-64 | 228 | See source audit package | Technical checks and BP1 passed; upstream byte-stream provenance absent | Strict contract correctly remained INCONCLUSIVE; BP2 not established |

Additional recorded identities:

- Starship runtime P6 PPM: 196,623 bytes; SHA-256 `97565975c7b49eeed6278f391aeb96803d3cc03d79d59b1747692e26d895569c`.
- LHC runtime RGBA: 55,296,000 bytes; SHA-256 `22e5742d9e9690deb42def9f292e2a2b5697a382eebda86b668c2a373f753b64`.
- Rising Sun runtime WAV: 40,320,044 bytes; SHA-256 `90be877fad9d99966b61a93c008a92bbb841a8e495c99c1e91b723f9b6379a3c`.

The portfolio supports a narrow claim: reconstructible exact-byte workflows were applied across multiple artifact types and behaviors with preserved failures, repairs, provenance distinctions, and an inconclusive strict audit. It does not estimate success probability or PARS advantage.

## 6. Limitations and interpretation

Always consider:

- historical selection and survivorship bias;
- incomplete prompt archives;
- generator/verifier correlation;
- upstream provenance gaps;
- runtime environment dependence;
- capture, scaling, muxing, or stitching distortion;
- subjective visual acceptance;
- absence of toolchain markers not proving BP2;
- model/configuration dependence;
- proof-display scaling limits;
- learned binary knowledge, prompt specificity, iterative debugging, and task-family selection as alternative explanations.

Possible prospective outcomes include improved CCEBS, improved classification without improved raw generation, improved reliability at significant cost, no meaningful difference, or worse performance. Publish all outcomes under frozen rules.

## 7. Evidence package structure

Use this logical layout:

```text
/PARS-EXPERIMENT-ID
|-- 00_README.md
|-- contract/target.md, invariants.json, prompt.txt
|-- generation/frozen_byte_stream.hex, byte_stream.sha256, generation_receipt.json
|-- artifact/artifact.bin, artifact.sha256
|-- reconstruction/reconstructed.bin, reconstructed.sha256, identity_receipt.txt
|-- inspection/format.txt, architecture.txt, structural_receipt.json
|-- runtime/execution_receipt.json, stdout.bin, stderr.bin, output/
|-- provenance/generation_path.md, prohibited_path_checks.json, hostile_tests/
|-- failures/candidate_*/, failure_ledger.json
|-- media/screenshots/, evidence_video.mp4
`-- results/PARS_FEBP_EVIDENCE_RECEIPT.json
```

Preserve immutable experiment IDs, hashes, exact prompt identity or an explicit missing-prompt statement, verifier identity, failed candidates, and final classification.
