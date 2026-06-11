# Contributing

## Project Purpose

Evidence-Bound Clinical Review Toolkit is a portfolio-grade prototype for healthcare-adjacent AI output review infrastructure.

It demonstrates how AI-generated draft text can be represented as a structured Clinical Review Packet with evidence links, missing-information flags, workflow risk routing, human review status, reviewer decisions, and audit events.

This project is not a clinical decision system, diagnostic tool, treatment recommendation system, patient-facing medical tool, production deployment, HIPAA-compliant system, or medical device.

## What Contributions May Add

Contributions may add or improve:

- schema structure
- synthetic examples
- review workflow documentation
- structural validation tests
- negative tests for malformed packets
- safety-boundary clarification
- README clarity
- documentation consistency checks

## What Contributions Must Not Add

Contributions must not add:

- real patient data
- diagnosis or treatment recommendation logic
- clinical correctness validation
- patient-facing medical advice
- autonomous medical decision-making
- claims of HIPAA compliance
- claims of production readiness
- claims of medical-device functionality
- real clinical deployment instructions

## Safety-Boundary Rules

All changes must preserve the repository's scope as review infrastructure only.

Do not frame schema validation, tests, examples, or documentation as proving clinical correctness, treatment safety, diagnostic accuracy, or real-world medical suitability.

Use synthetic examples only. Do not include protected health information, identifiable patient details, or real clinical records.

Workflow labels such as `risk_level` are review-routing labels, not clinical diagnoses, medical severity scores, or patient-specific risk assessments.

## Test Expectations

Tests may validate:

- packet structure
- required fields
- enum values
- malformed packet rejection
- documentation consistency if added later

Tests must not validate:

- clinical correctness
- treatment appropriateness
- diagnostic accuracy
- medical safety

## Documentation Expectations

Documentation should use clear professional English and maintain the safety boundary.

When adding examples or workflows, explicitly distinguish reviewability from clinical validation. Do not imply real patient use, autonomous medical decision-making, clinical deployment, HIPAA compliance, production readiness, or medical-device functionality.

