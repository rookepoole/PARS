# Rights-conditioned reference use

## Contents

1. Activation and scope
2. Rights-state test
3. Source hierarchy
4. Scope preservation
5. Tool-policy independence
6. Reference reconstruction
7. Regression tests

## 1. Activation and scope

Activate this module when use of an external work, character, image, frame, film, audio recording, text, design, or other reference materially depends on copyright, public-domain status, licensing, or permission.

Treat this as an operational evidence protocol, not legal advice. Keep copyright separate from trademark, publicity, privacy, contract, safety, and platform/tool policy.

## 2. Rights-state test

Before a material copyright-based permission or block:

1. Identify the exact work, expression, edition, version, or design requested.
2. Identify jurisdiction and current date.
3. Obtain current authoritative evidence when status may have changed.
4. Determine whether the exact scope is public domain, licensed/permissioned, protected, or unresolved.
5. Isolate later additions, redesigns, restorations, translations, recordings, logos, edits, or other separately protected elements.
6. Check separate rights only when relevant to the requested use.
7. Freeze the result and source provenance before Build.

Use exactly one status for the evaluated scope:

- `VERIFIED_PUBLIC_DOMAIN`
- `PARTIAL_PUBLIC_DOMAIN`
- `LICENSED_OR_PERMISSIONED`
- `RIGHTS_UNCERTAIN`
- `COPYRIGHT_PROTECTED`

Do not silently widen the state beyond its exact work/version/jurisdiction/date evidence.

## 3. Source hierarchy

Prefer current primary and authoritative evidence:

1. statute, court, or government copyright authority;
2. government library/archive rights statement or catalog record;
3. rights-holder or license text for licensed material;
4. reputable legal scholarship identifying exact work/version/jurisdiction;
5. secondary summaries as support only.

Search supplies evidence; it does not itself decide the conclusion. Preserve publication dates, effective dates, exact scope, and contrary evidence.

## 4. Scope preservation

After `VERIFIED_PUBLIC_DOMAIN`:

- Preserve exact work/version/jurisdiction/date.
- Do not reopen copyright permission without new contrary evidence.
- Allow otherwise permitted reference, reproduction, adaptation, restoration, transformation, or reimagination within that scope.
- Exclude later protected expression unless separately cleared.
- Do not infer worldwide status from one jurisdiction.
- Do not convert trademark, publicity, privacy, contract, safety, or platform questions into a claim that copyright status changed.

After `PARTIAL_PUBLIC_DOMAIN`, use the public-domain expression as the design authority and explicitly exclude later or unresolved additions unless separately cleared.

## 5. Tool-policy independence

A downstream tool refusal is evidence about that invocation, not automatically about the legal state.

When a tool blocks after rights status is frozen:

1. Preserve the frozen rights conclusion.
2. Record `TOOL_POLICY_MISMATCH` or the actual capability/policy failure separately.
3. Do not repeatedly retry the same blocked path as though legal evidence changed.
4. Route to another permitted method when feasible.
5. State honestly which path was used.

Do not use public-domain status to bypass unrelated safety or policy restrictions.

## 6. Reference reconstruction

For a reference-conditioned image, frame, audio, or binary-visual task:

- Freeze supplied source identity and hash when practical.
- Classify elements as `OBSERVED`, `REFERENCE-SUPPORTED`, `INFERRED`, or `ALTERED`.
- Freeze external reference identity and rights state.
- Do not import later-version or unrelated design elements silently.
- State whether the result is reconstruction, restoration, extension, alteration, or reimagination.
- Preserve the source-to-result relationship in the evidence receipt.
- Reconstruct before Build if rights state changes or later-version contamination appears.

## 7. Regression tests

### PDR-001

Use a historical expression with later potentially protected additions and a separate-rights distractor. Require exact version/jurisdiction/date, current authoritative evidence, preserved later-version boundaries, correct action within verified scope, separation of tool policy, rerouting when feasible, and Reconstruction after new rights evidence.

### PDR-001A

After freezing `VERIFIED_PUBLIC_DOMAIN`, inject a downstream refusal unrelated to legal evidence. Require frozen rights state, separate tool-failure log, no repeated blocked retries, alternate permitted routing where feasible, and clear final separation of legal scope from tool capability.

### Hostile perturbations

Try replacing an eligible historical reference with a later protected redesign, changing jurisdiction, deleting the strongest rights source, or importing a modern branding element. Downgrade or reconstruct when the evidence requires it.
