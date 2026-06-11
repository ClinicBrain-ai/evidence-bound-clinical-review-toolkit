# Documentation Index

This index helps reviewers, collaborators, and portfolio readers quickly find the right documentation for the Evidence-Bound Clinical Review Toolkit.

## Start Here

- [README.md](../README.md): Main project overview, workflow summary, safety boundary, test commands, and key links.
- [docs/PORTFOLIO_POSITIONING.md](PORTFOLIO_POSITIONING.md): Portfolio-facing explanation of the hiring signal, design choices, and safety-first scope.

## Understand the Project

- [docs/BEFORE_AFTER.md](BEFORE_AFTER.md): Concise before/after framing for converting AI-generated draft output into a reviewable packet.
- [docs/PORTFOLIO_POSITIONING.md](PORTFOLIO_POSITIONING.md): Explains why the project exists and what it demonstrates.
- [CHANGELOG.md](../CHANGELOG.md): Version-by-version summary of repository changes.

## Understand the Review Workflow

- [docs/REVIEW_WORKFLOW.md](REVIEW_WORKFLOW.md): Step-by-step review workflow from synthetic case summary to audit event.
- [docs/REVIEW_PACKET_LIFECYCLE.md](REVIEW_PACKET_LIFECYCLE.md): Packet states and outcomes explained as workflow metadata.
- [docs/REVIEW_DECISION_GUIDE.md](REVIEW_DECISION_GUIDE.md): Reviewer decision values explained as workflow outcomes, not clinical judgments.
- [docs/REVIEW_RUBRIC.md](REVIEW_RUBRIC.md): Simple rubric for evidence support, missing information, unsupported claims, scope creep, risk routing, and reviewer decision.

## Understand the Schema

- [docs/SCHEMA_FIELD_REFERENCE.md](SCHEMA_FIELD_REFERENCE.md): Field-by-field explanation of packet metadata and safety boundaries.
- [docs/REVIEW_PACKET_LIFECYCLE.md](REVIEW_PACKET_LIFECYCLE.md): Relationship between packet fields, workflow states, and packet outcomes.
- [docs/REVIEW_DECISION_GUIDE.md](REVIEW_DECISION_GUIDE.md): Definitions for allowed `review_status.decision` values.
- [schemas/clinical_review_packet.schema.json](../schemas/clinical_review_packet.schema.json): JSON Schema for Clinical Review Packet structure.

## Understand Examples

- [docs/EXAMPLE_REVIEW_PATTERNS.md](EXAMPLE_REVIEW_PATTERNS.md): Map of each synthetic example to its reviewability pattern.
- [examples/synthetic_dental_case_001/WALKTHROUGH.md](../examples/synthetic_dental_case_001/WALKTHROUGH.md): Step-by-step walkthrough of the synthetic dental example as a reviewability artifact.
- [examples/synthetic_dental_case_001/input_case_summary.md](../examples/synthetic_dental_case_001/input_case_summary.md): Synthetic source summary.
- [examples/synthetic_dental_case_001/ai_output.md](../examples/synthetic_dental_case_001/ai_output.md): AI-generated draft output.
- [examples/synthetic_dental_case_001/clinical_review_packet.json](../examples/synthetic_dental_case_001/clinical_review_packet.json): Structured example packet.
- [examples/synthetic_dental_case_001/reviewer_decision.md](../examples/synthetic_dental_case_001/reviewer_decision.md): Reviewer workflow decision note.
- [examples/synthetic_dental_case_002/WALKTHROUGH.md](../examples/synthetic_dental_case_002/WALKTHROUGH.md): Walkthrough of unsupported or over-specific AI output under incomplete source context.
- [examples/synthetic_dental_case_002/input_case_summary.md](../examples/synthetic_dental_case_002/input_case_summary.md): Second synthetic source summary.
- [examples/synthetic_dental_case_002/ai_output.md](../examples/synthetic_dental_case_002/ai_output.md): Second AI-generated draft output.
- [examples/synthetic_dental_case_002/clinical_review_packet.json](../examples/synthetic_dental_case_002/clinical_review_packet.json): Second structured example packet.
- [examples/synthetic_dental_case_002/reviewer_decision.md](../examples/synthetic_dental_case_002/reviewer_decision.md): Second reviewer workflow decision note.
- [examples/synthetic_dental_case_003/WALKTHROUGH.md](../examples/synthetic_dental_case_003/WALKTHROUGH.md): Walkthrough of conflicting source information preserved for review.
- [examples/synthetic_dental_case_003/input_case_summary.md](../examples/synthetic_dental_case_003/input_case_summary.md): Third synthetic source summary.
- [examples/synthetic_dental_case_003/ai_output.md](../examples/synthetic_dental_case_003/ai_output.md): Third AI-generated draft output.
- [examples/synthetic_dental_case_003/clinical_review_packet.json](../examples/synthetic_dental_case_003/clinical_review_packet.json): Third structured example packet.
- [examples/synthetic_dental_case_003/reviewer_decision.md](../examples/synthetic_dental_case_003/reviewer_decision.md): Third reviewer workflow decision note.

## Understand Safety Boundaries

- [docs/SAFETY_BOUNDARY.md](SAFETY_BOUNDARY.md): Concise safety boundary for healthcare-adjacent AI output review infrastructure.
- [docs/WHAT_THIS_IS_NOT.md](WHAT_THIS_IS_NOT.md): Explicit list of what the project does not do or claim.
- [CONTRIBUTING.md](../CONTRIBUTING.md): Contributor rules for allowed and prohibited future changes.

## Understand Development and Testing

- [README.md](../README.md#running-tests): Test setup and local test command.
- [requirements-dev.txt](../requirements-dev.txt): Development dependencies for tests.
- [pyproject.toml](../pyproject.toml): Project metadata and pytest configuration.
- [tests/](../tests): Required-field, schema validation, negative schema, and documentation safety consistency tests.

## Understand Roadmap and Version Scope

- [docs/VERSION_SCOPE.md](VERSION_SCOPE.md): What the v0.1.x series includes, excludes, and treats as future safe gates.
- [docs/ROADMAP.md](ROADMAP.md): Safe near-term improvements, medium-term portfolio improvements, out-of-scope work, and work requiring major scope review.
- [CHANGELOG.md](../CHANGELOG.md): Version history.

## Portfolio / Hiring-Signal Materials

- [docs/PORTFOLIO_POSITIONING.md](PORTFOLIO_POSITIONING.md): Main portfolio positioning document.
- [README.md](../README.md#hiring-signal): Short hiring-signal summary.
- [docs/BEFORE_AFTER.md](BEFORE_AFTER.md): Quick demonstration of the project transformation.
- [docs/EXAMPLE_REVIEW_PATTERNS.md](EXAMPLE_REVIEW_PATTERNS.md): Overview of the three synthetic review patterns.
- [examples/synthetic_dental_case_001/WALKTHROUGH.md](../examples/synthetic_dental_case_001/WALKTHROUGH.md): Concrete example walkthrough.

## Recommended Reading Paths

Portfolio reviewer:

1. [README.md](../README.md)
2. [docs/PORTFOLIO_POSITIONING.md](PORTFOLIO_POSITIONING.md)
3. [docs/BEFORE_AFTER.md](BEFORE_AFTER.md)
4. [examples/synthetic_dental_case_001/WALKTHROUGH.md](../examples/synthetic_dental_case_001/WALKTHROUGH.md)
5. [examples/synthetic_dental_case_002/WALKTHROUGH.md](../examples/synthetic_dental_case_002/WALKTHROUGH.md)
6. [examples/synthetic_dental_case_003/WALKTHROUGH.md](../examples/synthetic_dental_case_003/WALKTHROUGH.md)
7. [docs/WHAT_THIS_IS_NOT.md](WHAT_THIS_IS_NOT.md)

Technical reviewer:

1. [README.md](../README.md)
2. [docs/SCHEMA_FIELD_REFERENCE.md](SCHEMA_FIELD_REFERENCE.md)
3. [schemas/clinical_review_packet.schema.json](../schemas/clinical_review_packet.schema.json)
4. [tests/](../tests)
5. [CHANGELOG.md](../CHANGELOG.md)

Safety / boundary reviewer:

1. [docs/SAFETY_BOUNDARY.md](SAFETY_BOUNDARY.md)
2. [docs/WHAT_THIS_IS_NOT.md](WHAT_THIS_IS_NOT.md)
3. [CONTRIBUTING.md](../CONTRIBUTING.md)
4. [docs/EXAMPLE_REVIEW_PATTERNS.md](EXAMPLE_REVIEW_PATTERNS.md)
5. [docs/REVIEW_PACKET_LIFECYCLE.md](REVIEW_PACKET_LIFECYCLE.md)
6. [docs/REVIEW_DECISION_GUIDE.md](REVIEW_DECISION_GUIDE.md)
7. [docs/VERSION_SCOPE.md](VERSION_SCOPE.md)
8. [docs/ROADMAP.md](ROADMAP.md)
