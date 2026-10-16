# Security Policy

Thank you for helping us keep this project secure. This document explains how to report security vulnerabilities responsibly and how we will respond.

## Reporting a Vulnerability

Preferred (private) contact:
- Email: cristhianp3@gmail.com
  - Subject: [SECURITY] <short description>
  - Include: affected version (git commit/tag), detailed steps to reproduce, PoC (if safe), logs, and an indication whether you are willing to coordinate disclosure.

If you cannot use email, you may:
- Open an issue in this repository and include the word "security" in the title. **Do not** include exploit code or sensitive data in a public issue — contact the maintainer by email first.

If you prefer encrypted communication:
- Please encrypt sensitive reports using the project's PGP key (add key/fingerprint here if available). If no PGP key is published, use the email above and we will provide an upload mechanism for sensitive attachments.

## What to include in your report

To help us triage quickly, please include:
- Description of the issue and potential impact
- Steps to reproduce (minimal, reproducible example preferred)
- Affected versions / commit hash
- Any relevant logs or stack traces
- Proof of concept (PoC) or exploit details (only in private reports)
- Preferred contact method and timeline for disclosure

## Response & Timeline

We commit to:
- Acknowledge receipt within 72 hours.
- Triage the report and provide an initial assessment within 7 business days.
- Provide regular status updates until a fix or mitigation is available.
- Coordinate public disclosure and remediation timelines with the reporter.

Typical timelines (may vary based on severity and complexity):
- Acknowledgement: within 72 hours
- Initial triage: within 7 days
- Fix or mitigation: target within 90 days for most issues; critical issues will be prioritized and addressed faster where possible.

## Severity levels

We will classify issues by severity (example):
- Critical: remote code execution, data leakage of credentials, full compromise of systems.
- High: privilege escalation, significant data corruption, severe integrity issues.
- Medium: localized data exposure, significant denial of service to single components.
- Low: minor information leakage, UI issues, low-impact bugs.

Severity and remediation timelines will be set after initial triage.

## Coordinated Disclosure

- Please do not publicly disclose vulnerabilities until a mitigation or fix has been made available and we have coordinated a disclosure timeline with you.
- If you disclose before coordination, we will still respond, but coordinated disclosure helps users update safely.

## Supported Releases

- This repo currently ships as a demo and is maintained on the main branch.
- Please indicate the commit or tag you tested against when reporting an issue.
- If/when we publish formal releases (e.g., v0.1.0, v1.0.0), we will list supported versions and maintenance windows in this policy.

## After a fix

- We will credit reporters who request credit (unless they request anonymity) in our security acknowledgements.
- We may create a CVE for significant vulnerabilities and will coordinate attribution and timelines with the reporter.

## Dependencies & Supply‑chain

- If you suspect a vulnerability in a dependency, please report it here and indicate the package name and version. We will follow upstream disclosure processes and coordinate fixes.

## Miscellaneous

- Do not include sensitive information (private keys, passwords) in public issues or PR comments.
- If you discover leaked secrets in the repository, report them immediately via the contact method above; we will rotate or invalidate exposed credentials and provide follow-up guidance.

## Thank you

Thank you for taking the time to help keep this project safe. We value responsible disclosure and will work with you to remediate issues quickly and transparently.