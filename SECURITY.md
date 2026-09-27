# Security

## Scope

Security reports may concern the skill text, reusable templates, or any code in this repository. Include failures of containment or safety guidance that could expose users, credentials, or systems to harm.

## Report a vulnerability

If private vulnerability reporting is enabled, open the repository's **Security** tab, select **Report a vulnerability**, and submit a private report through GitHub. The reporting page is [New security advisory](https://github.com/rookepoole/PARS/security/advisories/new).

If that control is unavailable, request a private reporting channel through an issue without including vulnerability details. Keep exploit details, sensitive artifacts, and credentials out of public issues and discussions.

Include:

- The affected file and repository commit or version.
- The host, model, tools, and environment involved.
- A minimal reproduction, including the prompt or input and any relevant modifications.
- The expected safety boundary, observed behavior, and potential impact.
- Supporting logs or artifact hashes, with secrets and personal data removed.
- Any containment steps or mitigation already tested.

## Safe execution of binaries

Follow the [README safety guidance](README.md#safety):

- Statically inspect unknown or newly generated binaries before execution.
- Use a disposable, non-root, credential-free environment.
- Deny outbound networking by default and apply resource limits.
- Execute the independently reconstructed artifact, not an unrelated development copy.

Share inspection results and hashes before asking anyone to execute an artifact. A successful run does not establish safe behavior outside the tested environment.
