# Contribution Guidelines for EQDI

## Table of Contents
1. [Workflow](#workflow)  
2. [Code Standards](#code-standards)  
3. [Documentation](#documentation)  
4. [Issue Guidelines](#issue-guidelines)  
5. [Pull Request Process](#pull-request-process)  
6. [Community Standards](#community-standards)  
7. [Security Reporting](#security-reporting)  
8. [Legal](#legal)  

---

## Workflow

### 1. Repository Setup
- Fork the repository to your GitHub account.
- Clone your forked repository locally.
- Add the upstream repository for syncing changes.

### 2. Branch Naming
| Type              | Format               | Example                |
|-------------------|----------------------|------------------------|
| Feature           | `feat/description`   | `feat/quantum-scheduler` |
| Bug Fix           | `fix/issue-number`   | `fix/123-energy-bug`   |
| Documentation     | `docs/topic`         | `docs/contributing`    |

### 3. Commit Standards
- **Sign-off**: All commits must include a Developer Certificate of Origin (DCO) sign-off.
- **Conventional Commits**: Use the format `<type>(<scope>): <description>`.
  - Example: `fix(energy): correct solar harvesting thresholds`

---

## Code Standards

### Language-Specific Rules
| Language | Linter              | Formatter           | Test Framework |
|----------|---------------------|---------------------|----------------|
| Python   | Flake8              | Black               | pytest         |
| Rust     | Clippy              | rustfmt             | cargo-test     |
| Qiskit   | Qiskit Terra Checks | Qiskit Style Guide  | Qiskit Terra   |

### Testing Requirements
1. 90%+ test coverage for new features.
2. Integration tests for cross-component workflows.
3. Energy efficiency benchmarks for power-aware modules.

---

## Documentation

### Required Elements
1. **Python Docstrings**: Include detailed descriptions, arguments, and return values.
2. **Architecture Diagrams**: Store in `docs/architecture/`.
3. **Changelog Updates**: Document user-facing changes in `CHANGELOG.md`.

---

## Issue Guidelines

### Labels
| Label              | Purpose                                  | Color   |
|--------------------|------------------------------------------|---------|
| `good first issue` | Beginner-friendly                        | #00FF00 |
| `quantum`          | Requires Qiskit/PennyLane expertise      | #0000FF |
| `energy-critical`  | Affects power management                 | #FFA500 |

### Bug Reports
Required Fields:
1. Environment details (OS, Python version, hardware).
2. Reproduction steps.
3. Expected vs actual behavior.

---

## Pull Request Process

### Checklist
- [ ] Linked to GitHub Issue.
- [ ] Added/updated tests.
- [ ] Documentation updated.
- [ ] Passes CI/CD pipeline.
- [ ] Signed-off-by present.

### Review Process
1. **Initial Triage**: Within 48 hours.
2. **Expert Review**:
   - Quantum: @quantum-team
   - Energy: @energy-team
3. **Merge Approval**: Requires 2 maintainer approvals.

---

## Community Standards

### Code of Conduct
- Enforced [Contributor Covenant](CODE_OF_CONDUCT.md).
- Zero tolerance for:
  - AGPLv3 violations.
  - Corporate takeover attempts.

### Recognition
- Top contributors featured in `ACKNOWLEDGMENTS.md`.
- Monthly "EQDI Champion" badge for active members.

---

## Security Reporting

### Responsible Disclosure
1. Encrypt reports using the provided PGP key.
2. Email to security@eqdi.org with "[SECURITY]" subject.

---

## Legal

### Licensing
- All contributions licensed under AGPLv3.
- Patent grants via [Developer Certificate of Origin](https://developercertificate.org/).

### CLA Requirements
Contributors must:
1. Sign the [EQDI CLA](https://cla.eqdi.org).
2. Verify identity via SSH/GPG key.
