# Version Scope

## Purpose of the v0.1.x Series

The v0.1.x series establishes a portfolio-grade repository foundation for healthcare-adjacent AI output review infrastructure.

The focus is to make AI-generated draft output more reviewable through structured packet metadata, evidence traceability, missing-information flags, workflow routing labels, reviewer decisions, and audit events.

The v0.1.x series does not attempt to validate clinical correctness or support real patient care.

## What v0.1.x Includes

- repository foundation
- synthetic healthcare-adjacent example
- Clinical Review Packet schema
- schema validation tests
- negative schema tests
- pytest configuration
- contributor safety-boundary guide
- schema field reference
- documentation safety consistency tests

## What v0.1.x Intentionally Does Not Include

- real patient data
- diagnosis logic
- treatment recommendation logic
- clinical correctness validation
- medical safety validation
- autonomous review decisions
- patient-facing medical advice
- production deployment
- HIPAA compliance claims
- medical-device claims
- real clinical workflow integration

## Safety Boundary

This project remains review infrastructure only. It is not a clinical decision system, diagnostic tool, treatment recommendation system, patient-facing medical tool, production deployment, HIPAA-compliant system, or medical device.

Workflow labels, reviewer decisions, evidence links, missing-information flags, and audit events are packet metadata. They are not clinical judgments, medical safety determinations, legal compliance guarantees, or instructions for patient care.

## Future Safe Gates

Future safe gates may include:

- README portfolio clarity polish
- additional synthetic examples
- more structural schema tests
- review rubric clarification
- example walkthrough documentation
- documentation consistency improvements
- packet stub templates that do not make clinical judgments

## Gates That Should Not Be Added Without a Major Scope Review

The following gates should not be added without a major scope review:

- real patient data ingestion
- clinical decision support behavior
- diagnosis or treatment recommendation generation
- automated clinical risk scoring
- claims of HIPAA compliance
- production deployment instructions
- EHR integration
- clinician replacement workflows
- patient-facing advice workflows

