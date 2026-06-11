# Changelog

## v0.4.2

- Added owner-led GitHub release draft materials.
- Prepared safe release notes and owner review checklist.
- Added no runtime behavior.
- Added no clinical, compliance, production, or medical-device claims.

## v0.4.1

- Added explicit MIT LICENSE file.
- Aligned repository license file with project metadata.
- Added no runtime behavior.

## v0.4.0

- Completed portfolio package readiness review.
- Confirmed README, examples, documentation navigation, tests, and safety boundaries are ready for owner-led release drafting.
- Added no runtime behavior.
- Added no clinical, compliance, production, or medical-device claims.

## v0.3.7

- Added example review patterns documentation.
- Mapped each synthetic example to a distinct reviewability pattern.
- Reinforced that examples are synthetic review artifacts, not clinical assessments.

## v0.3.6

- Added third synthetic example.
- Demonstrated conflicting source information review pattern.
- Reinforced that the packet preserves reviewability and does not resolve clinical conflicts.

## v0.3.5

- Added schema-documentation consistency coverage for missing_information.status.
- Verified missing-information status labels in documentation match schema enum values.
- Reaffirmed that missing-information status is workflow metadata, not a clinical finding or treatment-gap determination.

## v0.3.4

- Added schema-documentation consistency coverage for risk_assessment.risk_level.
- Verified workflow risk labels in documentation match schema enum values.
- Reaffirmed that risk labels are workflow routing metadata, not clinical risk scores or medical severity labels.

## v0.3.3

- Added schema-documentation enum consistency test.
- Verified reviewer decision values documented in REVIEW_DECISION_GUIDE.md match the schema enum.
- Reaffirmed that the test validates workflow metadata consistency only.

## v0.3.2

- Added review decision guide.
- Defined reviewer decision values as workflow outcomes.
- Reinforced that decisions do not validate clinical correctness or medical safety.

## v0.3.1

- Added second synthetic example.
- Demonstrated repeatability across a second review situation.
- Updated schema validation to validate all example packets.
- Reinforced that examples are synthetic and not clinical assessments.

## v0.3.0

- Polished README as a flagship landing page.
- Added clearer before / after framing.
- Highlighted core workflow, demonstrations, non-claims, and start-here links.
- Reinforced safety-first portfolio positioning.

## v0.2.4

- Added review packet lifecycle documentation.
- Clarified packet states and outcomes as workflow metadata.
- Reinforced that packet lifecycle does not represent clinical status, diagnosis, treatment planning, or medical safety validation.

## v0.2.3

- Added internal Markdown link-check test.
- Improved documentation navigation reliability.
- Reaffirmed that tests validate structure, documentation boundaries, and repository navigation only.

## v0.2.2

- Added documentation index.
- Mapped core docs by reader need.
- Added recommended reading paths for portfolio, technical, and safety reviewers.

## v0.2.1

- Added roadmap documentation.
- Separated safe portfolio improvements from out-of-scope clinical, compliance, and deployment work.
- Clarified work requiring major scope review.

## v0.2.0

- Added portfolio positioning document.
- Clarified hiring signal and design choices.
- Reinforced safety-first scope and non-claims.

## v0.1.9

- Added synthetic example walkthrough.
- Explained the packet as a reviewability artifact.
- Reinforced that the walkthrough is not a clinical assessment.

## v0.1.8

- Added version scope documentation.
- Clarified what v0.1.x includes and intentionally excludes.
- Documented future safe gates and gates requiring major scope review.

## v0.1.7

- Added documentation safety consistency tests.
- Checked that core safety-boundary language remains present across README, CONTRIBUTING, and schema field reference.
- Reaffirmed that tests validate structure and documentation boundaries only, not clinical correctness.

## v0.1.6

- Added schema field reference documentation.
- Clarified packet fields as workflow metadata.
- Reinforced that risk labels and reviewer decisions are not clinical judgments.

## v0.1.5

- Added contributor safety-boundary guide.
- Clarified allowed and prohibited future changes.
- Reinforced that the project remains review infrastructure only.

## v0.1.4

- Added minimal pyproject.toml project metadata.
- Added pytest configuration for test discovery.
- Simplified the local test command to `python3 -m pytest`.
- Added no runtime behavior.

## v0.1.3

- Added negative schema tests for missing nested fields, invalid enum values, empty evidence arrays, and empty audit event arrays.
- Reaffirmed that tests validate packet structure only, not clinical correctness.

## v0.1.2

- Hardened the Clinical Review Packet JSON Schema with required nested workflow fields.
- Added structural enums for missing-information status, workflow risk level, review status, and reviewer decision.
- Updated the synthetic example packet to conform to the hardened schema without adding clinical claims.
- Clarified that schema validation checks structure only and that risk level is a workflow routing label, not a clinical risk score.

## v0.1.1

- Added development requirements for pytest and jsonschema.
- Added JSON Schema validation test for the synthetic Clinical Review Packet example.
- Documented test setup and clarified that tests validate packet structure only, not clinical correctness.

## v0.1.0

- Added initial repository foundation.
- Added safety and scope documentation.
- Added synthetic dental healthcare-adjacent example.
- Added Clinical Review Packet JSON schema.
- Added minimal pytest coverage for required packet fields.
