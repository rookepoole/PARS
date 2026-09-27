# Contributing to PARS

PARS welcomes changes that preserve the architecture's evidence discipline.

## Propose a change

Open an issue or [discussion](https://github.com/rookepoole/PARS/discussions) before proposing changes to `SKILL.md`, `references/`, or claim boundaries. Describe the problem, the intended change, and the evidence that would establish it. Keep each pull request focused on a reviewable change.

## Contribution rules

- Do not silently weaken user constraints or final invariants.
- Keep experimental, historical, prospective, and authoritative claims distinct.
- Preserve failed candidates, counterevidence, and rollback history when relevant.
- Add objective or held-out tests for strategy or controller promotion claims.
- Do not infer BP2 from BP1, BV2 from visual plausibility, or RL3 from prompting or memory.
- Keep `SKILL.md` procedural and concise; place detailed domain material in `references/`.
- Update `agents/openai.yaml` and `agents/anthropic.yaml` when the skill's user-facing identity changes.

## Before publishing a change

1. Validate YAML frontmatter and skill naming.
2. Verify every linked reference and template exists.
3. Preserve source hashes unless intentionally versioning a source artifact.
4. Test an inconsistent-contract case.
5. Test a provenance-gap case that must remain inconclusive.
6. Test a prospective benchmark prompt for correct claim boundaries.

Preserve the primary-source hashes recorded in [Source identity](README.md#source-identity). Any intentional source version change must be explicit and retain the prior source identity and relevant failure history.

See [Validation](README.md#validation) for the host-specific validation instructions and [source-authority.md](references/source-authority.md) for source roles and claim boundaries.
