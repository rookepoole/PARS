---
name: apply-pars-deep
description: Apply the PARS-Deep constraint-driven reasoning and verification procedure to substantive tasks while preserving hard constraints, mechanism-distinct alternatives, hostile tests, reconstruction after changed evidence, final-invariant replay, failure history, and evidence-bounded claims. Use when the user says to activate or use PARS/PARS-Deep; requests research-grade, exhaustive, high-stakes, contradictory-evidence, production, publication, long-horizon, causal, proof, audit, or next-best-move work; or needs freehand exact-binary generation, binary provenance, exact-byte repair, contained binary analysis, exact-byte visual classification, rights-conditioned reference use, PARS-FEBP prompts, evidence receipts, case studies, or benchmark design.
---

# Apply PARS Deep

## Operating rule

Apply PARS to the user's actual task. Produce the requested answer, artifact, decision, repair, audit, or experiment. Do not substitute a PARS implementation, framework summary, or process lecture unless the user explicitly requests one.

Keep private reasoning private. Surface the useful result, decisive evidence, uncertainty, material failures, claim boundary, deliverables, and next move. Let response length follow the user's need; a short response may still require full PARS-Deep reasoning.

Treat PARS v1.25.0-candidate.6 as an experimental, non-authoritative repair candidate. Do not claim that it is prospectively superior, generally validated, independently proven, or evidence of model-weight learning. Read [source-authority.md](references/source-authority.md) before making any PARS version, authority, historical-evidence, or validation claim.

## Route references

- Read [architecture-and-execution.md](references/architecture-and-execution.md) for any substantive PARS task, especially control, recursive search, invariants, adaptation, continuity, or failure handling.
- Read [exact-binary-protocol.md](references/exact-binary-protocol.md) when executable bytes, opaque binaries, provenance, exact repair, binary visuals, materialization, or contained execution are in scope.
- Read [rights-and-reference-use.md](references/rights-and-reference-use.md) when an external work, character, image, frame, film, audio recording, text, design, version, license, or public-domain claim determines what may be done.
- Read [evaluation-and-evidence.md](references/evaluation-and-evidence.md) for audits, evidence packages, case studies, benchmark design, ablations, receipts, historical examples, or performance claims.
- Read [prompt-protocols.md](references/prompt-protocols.md) when drafting or repairing a PARS-FEBP prompt, commissioning an independent audit, or choosing a reusable template.
- Read the raw [candidate specification](references/PARS_CANDIDATE_v1.25.0-candidate.6.md) or [whitepaper text](references/PARS_WHITEPAPER_PUBLIC_RELEASE_v1.0.txt) only when exact wording, a source-specific edge case, or deeper detail is necessary. Render the bundled [whitepaper PDF](references/PARS_WHITEPAPER_PUBLIC_RELEASE_v1.0.pdf) when figures or page layout matter.

For the long raw references, search before reading broadly. Useful patterns include:

```text
HARD_INVARIANT_SET|FINAL_INVARIANT_GATE|POST-BUILD|INCONSISTENT_CONTRACT
BP0|BP1|BP2|BP3|BV0|BV1|BV2|BV3|RL0|RL1|RL2|RL3
COVERAGE_CHALLENGE|TEST_VALUE|RISK_GUARD|INCONCLUSIVE_CONTROL
PARS-FEBP|CCEBS|BVIS-001|PDR-001|RFS-001|RLA-001|RCA-001|FIG-001
```

## Execute the canonical cycle

Use `Parse -> Branch -> Transform -> Perturb -> Test -> Reconstruct -> Build`. Combine stages for efficiency only when every applicable capability remains present. Return to an earlier stage when new evidence exposes a missing mechanism, defective representation, insufficient robustness, changed evidence, or changed contract.

### 1. Parse the contract

Freeze an evaluable task state before committing:

- Identify the actual objective, requested artifact, observable success, and failure conditions.
- Separate facts, assumptions, preferences, unknowns, and current-information needs.
- Preserve explicit negative constraints, including prohibited tools or generation paths.
- Freeze rights/version/jurisdiction/date state when external references determine scope.
- Freeze BP/BV claim targets for exact-binary work and RL class for adaptation claims.
- State the narrowest claim the available evidence could support.
- Record whether Build can mutate an acceptance-critical property.

Create a `HARD_INVARIANT_SET` for every acceptance-critical requirement. Give each invariant a stable ID, source, predicate, scope, strongest feasible verifier, and status (`ACTIVE`, `SUPERSEDED`, or `UNRESOLVED_CONTRACT`). Propagate active invariants to every branch and descendant.

If hard requirements conflict, return `INCONSISTENT_CONTRACT`; do not silently weaken one. If a material user choice cannot be inferred safely, request that choice.

### 2. Branch and control search

Generate mechanism-distinct alternatives, not paraphrases. For Deep work, use five or more branches when justified. Always preserve a NULL/OTHER possibility when noise, measurement error, environmental effects, selection effects, or an unmodeled mechanism could change the result.

Before robust commitment, run `COVERAGE_CHALLENGE`: identify any plausible observation or mechanism class that could materially change the action or claim but is not explained by the current branches. Branch again when one exists.

Rank feasible tests by `TEST_VALUE`: prefer evidence that can change the action, surviving branch set, claim boundary, Reconstruction state, or important tail risk relative to cost. Apply `RISK_GUARD`: do not prune a severe low-probability NULL/OTHER risk when a reasonably discriminating check is feasible.

Use bounded recursive fan-out only when subsearch can reduce decision-relevant uncertainty, expose a new mechanism, distinguish actions, or repair a known failure. Preserve parent/child lineage, inherited constraints, evidence provenance, stopped subtrees, remaining budget, and duplicate penalties. Do not recurse to inflate branch count.

Use the control states precisely:

- `CONTINUE`: a feasible next action has meaningful decision or robustness value.
- `STOP`: completion gates and coverage are adequate and no feasible remaining test has meaningful value; continue to Build.
- `INCONCLUSIVE_CONTROL`: reasonable interpretations imply materially different next actions; identify the estimate or evidence that must be narrowed.

### 3. Transform and perturb

Change representation when it exposes structure or failure. Useful transforms include count to rate, global graph to local dependencies, conjecture to minimal counterexample, symptom to state/event flow, codebase to authority/dependency graph, and failure to invariant violation. Preserve units, constraints, and coordinate frames.

Attack the leading candidate with at least one hostile perturbation capable of falsifying it. Consider boundary changes, corrupted or missing data, assumption deletion, evidence reorder, contradictory authority, implementation failure, provenance correction, prohibited-path contamination, later-version contamination, and finished-payload contamination. Record whether the result is stable or fragile. Reject, weaken, or materially revise at least one branch before claiming robust discrimination when feasible.

### 4. Test discriminating predictions

Prefer evidence in this order when applicable: proof or counterexample; independent measurement; controlled experiment; held-out prediction; reproducible simulation; historical replay; expert or source comparison; visual inspection; intuition.

For each important test preserve the method, result, criterion, limitations, version/time/hash where relevant, and evidence that the check actually ran. Freeze predictions before hidden outcomes when practical. Never treat one successful run, attractive output, repetition, confidence, or absence of a searched-for counterexample as decisive by itself.

### 5. Reconstruct after changed evidence

When evidence is invalid, corrected, contradictory, or late:

- Remove its influence without erasing history.
- Insert corrected evidence and recompute confidence.
- Rebuild every affected dependency and rerun downstream tests.
- Preserve unaffected work and failed candidates.
- Merge surviving partial branches only after resolving or exposing contradictions.
- Revise the claim boundary and adaptation records.
- Ask whether the result survives deletion of its strongest supporting assumption.

Classify the reconstructed state as `ROBUST`, `FRAGILE`, `REPAIRED`, `COLLAPSED`, or `INCONCLUSIVE`.

### 6. Run the Final Invariant Gate

Immediately before Build, instantiate the exact final candidate and replay every `ACTIVE` invariant with the strongest feasible verifier:

- On `PASS`, retain the receipt.
- On `FAIL`, mark `INVALID_FINAL_STATE`, preserve the violated predicate and evidence, forbid Build, and return to Reconstruction or search.
- On `UNVERIFIABLE`, obtain evidence if feasible; otherwise return an explicit inconclusive or contract-limited result.

Do not replace final replay with branch notes, sampled checks, majority vote, confidence, or prior partial success. Prefer a verifier independent of the generation path.

### 7. Build and replay materialization-sensitive invariants

Produce the requested result; a plan is not completion when execution was requested. If writing, rendering, serializing, packaging, compiling, compressing, or another Build step can change an invariant, freeze the built artifact identity and replay every affected invariant.

On post-Build failure, mark `INVALID_BUILT_ARTIFACT`, preserve the failure, repair or rebuild, and rerun the affected gate. Deliver an artifact as passing only after the actual materialized object passes.

### 8. Bound the claim and present the result

State only the strongest conclusion supported by evidence. Distinguish observed, reproduced, empirically supported, model-dependent, conjectured, proved, disproved, prospective, historical, synthetic, aesthetic, or implementation-hypothesis claims as appropriate.

Explicitly state what the result establishes, what stronger claim it does not establish, and what evidence would be needed for promotion. Preserve failures, repairs, caveats, reproducibility information, and the exact next best move without dumping private reasoning.

## Adaptation and controller changes

Classify learning claims conservatively:

- `RL0`: evidence changes the current task's search or reasoning policy.
- `RL1`: a reusable strategy is retained with trigger, operator, expected effect, evidence, scope, counterevidence, provenance/version, and status.
- `RL2`: a controller change is promoted after frozen parent-versus-child evaluation.
- `RL3`: model parameters are updated through an actual training mechanism.

Do not infer RL3 from prompting, context, memory, search, controller edits, or repeated inference. Do not promote a strategy or controller from self-approval. Prefer deterministic verification, held-out labels, frozen benchmarks, independent measurement, or evaluator separation. Preserve immutable parents, mutation receipts, failed children, leakage findings, rollback points, and negative-transfer evidence.

## Long-horizon continuity

Maintain one primary source of truth. Preserve artifact authority, contract and invariant state, failures, claim boundaries, completed work, rights/provenance locks, controller lineage, benchmark splits, and rollback points. Retrieve every affected cold-state dependency before Reconstruction. Do not repeat completed steps or silently turn a scoped heuristic into a universal rule.

## Templates

Copy and fill these assets when the user requests a durable record:

- [PARS-FEBP evidence receipt](assets/pars-febp-evidence-receipt.md)
- [PARS-ECS case study](assets/pars-ecs-case-study.md)
- [PARS-FEBP benchmark preregistration](assets/pars-febp-benchmark-preregistration.md)

Keep the original templates unchanged and write completed copies to the user's requested output location.
