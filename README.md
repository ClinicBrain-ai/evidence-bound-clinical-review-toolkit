# Evidence-Bound Clinical Review Toolkit

Evidence-Bound Clinical Review Toolkit is a portfolio-grade prototype for converting AI-generated healthcare-adjacent outputs into evidence-linked, human-reviewable Clinical Review Packets.

It demonstrates review infrastructure around AI-generated healthcare-adjacent text: what evidence the draft relied on, what context is missing, whether human review is required, what reviewer decision was made, and what audit events were recorded.

## Before / After

Before:

AI generated a fluent healthcare-adjacent summary, but reviewers could not easily verify what evidence it relied on, what context was missing, whether human review was required, or what decision was made.

After:

The same output is represented as a Clinical Review Packet with source evidence, missing-information flags, workflow risk labels, human review requirements, reviewer decisions, and audit events.

## Core Workflow

```text
Synthetic case summary
  -> AI-generated draft output
  -> Clinical Review Packet
  -> Evidence + missing context
  -> Workflow risk label
  -> Human review decision
  -> Audit events
```

## Relationship To Evaluation Harness

The [Evidence-Bound AI Evaluation Harness](https://github.com/ClinicBrain-ai/evidence-bound-ai-evaluation-harness) sits one step before this toolkit. It reviews an AI-generated healthcare-adjacent output for evidence support, unsupported claims, missing context, uncertainty gaps, source conflicts, scope-boundary issues, and human-review routing.

This toolkit then turns bounded healthcare-adjacent material into a Clinical Review Packet for human review. The relationship is workflow-oriented: evaluation report first, review packet second. Neither repository validates clinical correctness, recommends treatment, assesses medical safety, claims HIPAA compliance, or supports clinical deployment.

## What This Demonstrates

- evidence-bound AI output review
- missing-context awareness
- human-in-the-loop workflow design
- reviewability and traceability
- workflow risk routing
- reviewer decision capture
- audit-ready workflow metadata
- safety-boundary discipline

The target identity for this project is a dentist-trained builder of healthcare AI workflow and evaluation infrastructure.

See [docs/PORTFOLIO_POSITIONING.md](docs/PORTFOLIO_POSITIONING.md) for the portfolio-facing positioning, hiring signal, design choices, and safety-first scope.

## What This Does Not Do

This project does not:

- diagnose patients
- recommend treatment
- validate clinical correctness
- assess medical safety
- provide patient-facing medical advice
- replace clinicians or licensed reviewers
- claim HIPAA compliance
- claim production readiness
- function as a medical device
- use real patient data

## Start Here

- [Documentation Index](docs/DOCUMENTATION_INDEX.md): quick navigation by reviewer need
- [Portfolio Positioning](docs/PORTFOLIO_POSITIONING.md): hiring signal, design choices, and safety-first scope
- [Before / After](docs/BEFORE_AFTER.md): concise transformation from fluent draft to reviewable packet
- [Synthetic Example 001 Walkthrough](examples/synthetic_dental_case_001/WALKTHROUGH.md): missing context around a plausible AI-generated draft
- [Synthetic Example 002 Walkthrough](examples/synthetic_dental_case_002/WALKTHROUGH.md): unsupported or over-specific AI output under incomplete source context
- [Synthetic Example 003 Walkthrough](examples/synthetic_dental_case_003/WALKTHROUGH.md): conflicting source information preserved for review
- [Example Review Patterns](docs/EXAMPLE_REVIEW_PATTERNS.md): why each synthetic example exists
- [Schema Field Reference](docs/SCHEMA_FIELD_REFERENCE.md): packet fields explained as workflow metadata
- [Safety Boundary](docs/SAFETY_BOUNDARY.md): concise project boundary
- [Version Scope](docs/VERSION_SCOPE.md): what the current series includes and excludes
- [Roadmap](docs/ROADMAP.md): safe future work and work requiring major scope review

## Synthetic Examples

The included examples are de-identified synthetic dental scenarios. Each contains:

- an input case summary
- a plausible AI-generated draft output
- a structured Clinical Review Packet
- a reviewer decision note

Case 001 demonstrates missing context around a plausible AI-generated draft that references possible infection or inflammation. The packet flags missing recent imaging, medication history, allergy information, and periodontal assessment.

Case 002 demonstrates unsupported or over-specific AI output under incomplete source context. The packet flags missing procedure details, recent imaging, medication history, allergy information, clinician exam findings, and unsupported cause language.

Case 003 demonstrates conflicting source information. The packet preserves differing source descriptions, missing timing context, and the reviewer workflow decision without resolving the conflict clinically.

See [docs/EXAMPLE_REVIEW_PATTERNS.md](docs/EXAMPLE_REVIEW_PATTERNS.md) for a concise map of the review pattern each synthetic example demonstrates.

See [examples/synthetic_dental_case_001/WALKTHROUGH.md](examples/synthetic_dental_case_001/WALKTHROUGH.md), [examples/synthetic_dental_case_002/WALKTHROUGH.md](examples/synthetic_dental_case_002/WALKTHROUGH.md), and [examples/synthetic_dental_case_003/WALKTHROUGH.md](examples/synthetic_dental_case_003/WALKTHROUGH.md) for step-by-step explanations of the examples as reviewability artifacts, not clinical assessments.

## Running Tests

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest
```

The tests validate Clinical Review Packet structure and JSON Schema conformance only. They do not validate clinical correctness, diagnosis, treatment safety, treatment recommendations, medical advice, or patient-specific advice.

Positive schema tests confirm the example packets have valid packet structure. Negative schema tests confirm malformed packet structures are rejected. These tests do not validate clinical correctness or medical safety.

Documentation consistency tests help ensure key safety-boundary language remains present. These tests still do not validate clinical correctness, medical safety, diagnosis, or treatment appropriateness.

Markdown link-check tests help keep repository navigation intact. These tests validate documentation links only, not clinical correctness or medical safety.

Enum consistency tests help ensure documented workflow metadata values match the JSON Schema. These tests validate schema-documentation consistency only, not clinical correctness, patient risk, medical severity, diagnosis, treatment appropriateness, or medical safety.

## Packet Metadata

The packet `risk_level` is a workflow routing label for review infrastructure. It is not a clinical diagnosis, medical severity score, or validation of patient-specific risk.

Reviewer decisions are workflow decisions, not proof of clinical correctness. Source evidence supports traceability, not medical correctness. Audit events preserve workflow history, not compliance guarantees.

## Key Documentation

- [docs/DOCUMENTATION_INDEX.md](docs/DOCUMENTATION_INDEX.md): navigation guide organized by reviewer need
- [docs/REVIEW_PACKET_LIFECYCLE.md](docs/REVIEW_PACKET_LIFECYCLE.md): packet states and outcomes as workflow metadata
- [docs/REVIEW_DECISION_GUIDE.md](docs/REVIEW_DECISION_GUIDE.md): reviewer decision values as workflow outcomes
- [docs/SCHEMA_FIELD_REFERENCE.md](docs/SCHEMA_FIELD_REFERENCE.md): field-by-field explanations and safety boundaries
- [docs/VERSION_SCOPE.md](docs/VERSION_SCOPE.md): version scope and future gates
- [docs/ROADMAP.md](docs/ROADMAP.md): safe portfolio improvements and out-of-scope work
- [docs/RELEASE_DRAFT_V0_4_2.md](docs/RELEASE_DRAFT_V0_4_2.md): owner-reviewed release draft materials
- [docs/public/LINKEDIN_BUILD_NOTE_V0_4_2.md](docs/public/LINKEDIN_BUILD_NOTE_V0_4_2.md): conservative public sharing draft for the v0.4.2 release
- [CONTRIBUTING.md](CONTRIBUTING.md): safety-boundary rules, allowed contribution types, prohibited changes, and test expectations

## License

MIT

## Safety Boundary

The toolkit is limited to review infrastructure for healthcare-adjacent AI output. It is intended to show how outputs can be organized for human review, not how clinical decisions should be made.

No content in this repository should be used for real patient care, clinical deployment, diagnosis, treatment recommendation, patient-facing advice, second opinions, autonomous medical decision-making, HIPAA compliance claims, production readiness claims, or medical-device functionality.

## Hiring Signal

This repository is designed to show practical judgment around healthcare AI systems: separating fluent AI text from reviewable evidence, making uncertainty visible, using explicit safety boundaries, and designing lightweight audit infrastructure without overstating clinical capability.
