# PARS-Deep architecture and execution reference

## Contents

1. Canonical engine
2. Experimental control
3. Recursive search
4. Hard-invariant system
5. Evidence and Reconstruction
6. Adaptation and controller lineage
7. Failure and continuity state
8. Regression families

## 1. Canonical engine

Execute:

`Parse -> Branch -> Transform -> Perturb -> Test -> Reconstruct -> Build`

Keep every stage available. Return to Branch for a missing mechanism, Transform for a defective representation, Perturb for insufficient robustness, Reconstruct for changed evidence, and Parse for a changed contract.

Use PARS-Deep for research-grade, exhaustive, high-stakes, causal, proof, contradictory-evidence, production, publication, long-horizon, multiple-authority, durable-result, next-best-move, uncertain provenance, audit, repair, exact-byte, binary-visual, and materially rights-conditioned tasks. Brevity does not downgrade required depth.

## 2. Experimental control

### COVERAGE_CHALLENGE

Before robust commitment, ask which plausible observation or mechanism could change the action or claim but remains unexplained. Seek mechanism diversity, not branch-count inflation. Preserve NULL/OTHER.

### TEST_VALUE

Prefer the valid test with the greatest decision-relevant value relative to cost. Value includes changing the selected action, branch set, claim boundary, Reconstruction state, or important tail risk. Use defensible numbers only when available; otherwise use ranges or orderings.

### RISK_GUARD

Do not suppress a severe low-probability NULL/OTHER branch when a reasonably discriminating check is feasible at acceptable cost.

### Control states

- `CONTINUE`: a feasible next action can materially improve the decision, claim, defect state, Reconstruction, or tail-risk coverage.
- `STOP`: completion gates, branch coverage, and tail-risk checks are adequate and no feasible remaining test has meaningful value. STOP ends evidence acquisition, not Build.
- `INCONCLUSIVE_CONTROL`: reasonable estimates imply different next actions. Identify and narrow the unstable estimate rather than fabricating precision.

Control may schedule valid PARS actions. It may not override hard constraints, safety, containment, evidence/provenance integrity, hostile perturbation, failure preservation, Reconstruction, claim boundaries, or final verification.

## 3. Recursive search

Fan out a branch into a bounded PARS subcycle only when:

1. decision-relevant uncertainty remains;
2. at least two mechanism-distinct continuations are plausible;
3. continuations make different predictions, expose different failures, or change Build;
4. expected information or robustness gain justifies the work.

Preserve subproblem, mechanism, assumptions, inherited constraints, evidence provenance, test target, failures, remaining budget, and parent/child lineage. Prioritize decision relevance, uncertainty reduction, mechanism novelty, falsifiability, tail-risk coverage, repair ability, and feasible cost. Penalize semantic duplicates.

Stop a subtree when it is falsified, dominated, subsumed without loss, untestable, duplicative, or too costly for plausible decision value. Preserve stopped/rejected subtrees in history. Never spend the entire search budget on an attractive subtree while pruning a decisive NULL/OTHER branch.

## 4. Hard-invariant system

Represent every acceptance-critical condition as:

```text
ID:
Source: user | authoritative specification | derived necessity | safety/containment | accepted test contract
Predicate:
Scope:
Verifier:
Status: ACTIVE | SUPERSEDED | UNRESOLVED_CONTRACT
```

Before Build, replay every ACTIVE invariant on the exact selected candidate.

- Any FAIL -> `INVALID_FINAL_STATE`; forbid Build and return to Reconstruction/search.
- Any UNVERIFIABLE -> obtain evidence or return inconclusive.
- Contradictory predicates -> `INCONSISTENT_CONTRACT`; return to Parse.
- All PASS -> Build may begin.

After materialization, replay every invariant that Build could have changed. Any failure -> `INVALID_BUILT_ARTIFACT`; block delivery, repair, rebuild, and retest.

The final gate evaluates the actual final object. Branch confidence, majority vote, earlier partial checks, and aesthetic quality cannot override it.

## 5. Evidence and Reconstruction

Rank evidence, strongest first:

1. proof/counterexample
2. independent measurement
3. controlled experiment
4. held-out prediction
5. reproducible simulation
6. historical replay
7. expert/source comparison
8. visual inspection
9. intuition

Count duplicated evidence once. Treat authority as affecting reliability, not truth. Replace defective influence with corrected evidence without double-counting both. Preserve decisive counterexamples and the fact that a check actually ran.

After material evidence changes, remove invalid influence, insert corrections, recompute confidence, rebuild affected dependencies, rerun downstream tests, preserve unaffected work, revise claims, and keep failure history. Try deleting the strongest supporting assumption and, when relevant, one source, criterion, authority, measurement channel, or coordinate frame.

Use `ROBUST`, `FRAGILE`, `REPAIRED`, `COLLAPSED`, or `INCONCLUSIVE` for the reconstructed state.

## 6. Adaptation and controller lineage

Use these learning classes:

- RL0: current-task adaptation only.
- RL1: verified scoped strategy memory.
- RL2: verified controller adaptation after parent-versus-child evaluation.
- RL3: actual parameter learning through training.

Each RL1 record preserves trigger, operator, expected effect, evidence, scope, counterevidence/failures, provenance/version, and status (`CANDIDATE`, `VERIFIED_SCOPED`, `REJECTED`, `STALE`, or `REVALIDATION_REQUIRED`). Retrieval is not new evidence.

Treat controller changes as children. Freeze the parent and preserve a mutation receipt containing exact changed rules, predicted benefit, predicted regression, benchmark, and resource expectation.

Use the lineage:

`PARENT_FROZEN -> CHILD_PROPOSED -> CHILD_TESTING -> PROMOTED | REJECTED | INCONCLUSIVE -> optional repair -> RETEST`

Require objective or held-out promotion evidence. Invalidate leaked benchmark items. Preserve rejected children and rollback to the last passing controller after material regression.

## 7. Failure and continuity state

Preserve what failed, why, impact, repair, retest, and whether the conclusion changed. Do not erase failed benchmarks, rejected hypotheses, environment failures, stale strategies, poisoned memory, leakage, or rollbacks.

For long projects preserve one primary source of truth, authority relationships, contract/invariants, evidence provenance and independence, branch state, test receipts, artifacts, failures, claim boundary, current gate, exact next move, recursive lineage, strategy records, controller versions, benchmark split identity, and rollback point.

## 8. Regression families

Use these named candidate.6 regression families when testing PARS itself:

- `RFS-001`: fan-out value against predecessor, breadth-only, and no-Reconstruct ablations.
- `RLA-001`: strategy transfer with development, transfer, and negative-transfer cohorts.
- `RCA-001`: frozen parent-versus-child controller promotion.
- `RCA-001A`: self-judge contamination.
- `RCA-001B`: benchmark leakage.
- `RCA-001C`: rollback after fresh regression.
- `RLA-002`: stale or poisoned strategy memory.
- `RFS-002`: search explosion and branch starvation.
- `FIG-001`: full invariant replay on a near-solution with one nonlocal violation.
- `FIG-001A`: post-Build mutation.
- `FIG-001B`: inconsistent contract.
- `FIG-001C`: unverifiable hard invariant.

Treat old development failures, including HSCH-02, as development evidence rather than held-out promotion evidence.
