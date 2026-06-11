# Roadmap

## Roadmap Purpose

This roadmap separates safe portfolio improvements from work that is out of scope or requires major scope review.

The project remains a portfolio-grade prototype for healthcare-adjacent AI output review infrastructure. It is not a clinical decision system, diagnostic tool, treatment recommendation system, patient-facing medical tool, production deployment, HIPAA-compliant system, or medical device.

## Current Project Status

The project currently includes:

- synthetic healthcare-adjacent example
- Clinical Review Packet schema
- schema validation tests
- negative schema tests
- documentation safety consistency tests
- contributor safety rules
- schema field reference
- version scope documentation
- portfolio positioning documentation

## Safe Near-Term Improvements

Safe near-term improvements may include:

- README landing page polish
- additional synthetic examples
- clearer example walkthroughs
- review rubric clarification
- more structural validation tests
- documentation consistency improvements
- field reference refinements
- package navigation improvements

## Medium-Term Portfolio Improvements

Medium-term portfolio improvements may include:

- packet stub templates that do not make clinical judgments
- additional synthetic case categories
- review pattern library
- lightweight structural helper scripts
- example evaluation reports based only on structure and reviewability
- improved portfolio documentation

## Explicitly Out-of-Scope Work

This roadmap does not include:

- real patient data
- diagnosis generation
- treatment recommendation generation
- clinical correctness validation
- medical safety validation
- patient-facing medical advice
- clinician replacement
- real clinical workflow deployment
- EHR integration
- HIPAA compliance claims
- medical-device claims
- production deployment instructions

## Work Requiring Major Scope Review

The following work requires major scope review before it should be considered:

- any use of real patient data
- any workflow that could affect patient care
- any clinical decision support behavior
- any automated risk scoring that could be interpreted clinically
- any patient-facing output
- any deployment into a real healthcare setting
- any compliance or medical-device positioning

## Safety Boundary

This roadmap supports review infrastructure only. It does not authorize clinical functionality, patient-facing use, real healthcare deployment, HIPAA compliance claims, production readiness claims, or medical-device positioning.

Future work should preserve the distinction between making AI-generated healthcare-adjacent output reviewable and making clinical judgments.

