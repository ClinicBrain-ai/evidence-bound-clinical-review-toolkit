# Schema Field Reference

This document explains the major Clinical Review Packet fields as workflow metadata.

The schema validates packet structure only. It does not validate clinical correctness, diagnostic accuracy, treatment appropriateness, medical safety, patient-specific risk, production readiness, HIPAA compliance, or medical-device functionality.

## packet_id

Purpose: Provides a stable identifier for a review packet.

What it captures: A unique string that can be used to reference the packet in examples, tests, documentation, or audit records.

What it does not capture: It does not identify a real patient, clinical encounter, diagnosis, or treatment plan.

Safety boundary: Use synthetic identifiers only. Do not include protected health information or real patient identifiers.

## case_type

Purpose: Describes the broad category of the packet.

What it captures: A structural label such as synthetic dental healthcare-adjacent summary.

What it does not capture: It does not classify a real clinical condition or determine medical urgency.

Safety boundary: Treat this as workflow metadata, not clinical categorization.

## ai_output_type

Purpose: Describes the type of AI-generated draft being reviewed.

What it captures: A structural label such as draft summary.

What it does not capture: It does not indicate that the AI output is correct, safe, complete, or clinically appropriate.

Safety boundary: AI-generated output remains unverified draft text until reviewed within the intended non-clinical workflow context.

## original_ai_output

Purpose: Preserves the AI-generated draft output that is being reviewed.

What it captures: The original draft text in `original_ai_output.text`.

What it does not capture: It does not represent a diagnosis, treatment recommendation, second opinion, patient-facing advice, or clinically validated output.

Safety boundary: The stored text is review input only. It should not be treated as clinical guidance.

## source_evidence

Purpose: Records traceability between the packet and provided source material.

What it captures: Evidence item identifiers, source references, excerpts, and the draft element each item supports.

What it does not capture: Source evidence does not prove that a clinical statement is medically correct. It only shows that a packet statement traces to provided source material.

Safety boundary: Evidence links support reviewability, not clinical validation.

## missing_information

Purpose: Makes absent, unknown, present, or not applicable context explicit for reviewers.

What it captures: A field name, structural status, and reason for the flag.

Allowed workflow status labels:

- `missing`: expected context is absent from the provided material
- `present`: the context is present in the provided material
- `unknown`: the packet cannot determine whether the context exists from the provided material
- `not_applicable`: the field is not relevant to the packet's workflow context

What it does not capture: Missing information does not determine a diagnosis, treatment gap, clinical deficiency, or patient-specific medical risk.

Safety boundary: Missing-information flags are workflow documentation labels and review prompts, not clinical findings, treatment-gap determinations, or clinical conclusions.

## risk_assessment

Purpose: Supports workflow routing for human review.

What it captures: A structural `risk_level` label and a reason for the routing label.

Allowed workflow labels: `low`, `medium`, and `high`.

What it does not capture: `risk_level` is not a clinical diagnosis, medical severity score, patient risk score, or validation of clinical urgency.

Safety boundary: Risk labels are review-routing metadata only. They should not be used for clinical triage, patient advice, or autonomous medical decision-making.

## review_requirement

Purpose: States whether human review is required before downstream use within this prototype workflow.

What it captures: A boolean human-review requirement and the workflow reason for review.

What it does not capture: It does not determine whether a real patient needs care, whether a clinician must take action, or whether an output is medically safe.

Safety boundary: Human review requirement is a prototype workflow control, not a clinical instruction.

## review_status

Purpose: Records the review state and reviewer workflow decision.

What it captures: Review status, reviewer role, reviewer decision, and reviewer comment.

What it does not capture: `review_status.decision` is not proof of clinical correctness, diagnostic accuracy, treatment safety, or medical appropriateness.

Safety boundary: Reviewer decisions are workflow decisions about the packet, not clinical judgments about a patient.

## audit_events

Purpose: Records workflow events for traceability.

What it captures: Event type, timestamp, actor, and details for packet-related actions.

What it does not capture: Audit events do not guarantee legal compliance, HIPAA compliance, production readiness, clinical governance, or medical-device auditability.

Safety boundary: Audit events support prototype traceability only.
