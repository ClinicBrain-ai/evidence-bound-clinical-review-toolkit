# Review Decision Guide

This guide defines `review_status.decision` values as workflow outcomes.

Reviewer decisions in this repository do not validate clinical correctness, assess medical safety, provide patient-facing advice, recommend treatment, or replace clinicians or licensed reviewers.

## approved

Workflow meaning: The packet passed the defined review workflow criteria for the intended non-clinical context.

When it may be used: Use `approved` when the packet is structurally complete, the draft stays within supported source material, missing context is visible, and no workflow revision is required.

What it does not mean: It does not mean the AI output is clinically correct, diagnostically accurate, medically safe, or appropriate for patient care.

Non-clinical example: A reviewer approves a packet because all required fields are present, source excerpts are linked, and the draft remains limited to source-supported summary language.

## requires_revision

Workflow meaning: The output needs changes before downstream workflow use.

When it may be used: Use `requires_revision` when the packet identifies unsupported wording, unclear evidence mapping, missing-context flags that need clearer wording, or scope creep that can be corrected.

What it does not mean: It does not mean a diagnosis or treatment plan was determined.

Non-clinical example: A reviewer marks a packet as requiring revision because the draft describes a cause that is not supported by the provided source summary.

## rejected

Workflow meaning: The output should not proceed in the workflow.

When it may be used: Use `rejected` when the draft cannot be responsibly revised within the intended review workflow, such as when it is too unsupported, too patient-facing, or too far outside the project boundary.

What it does not mean: It does not mean a clinical claim was adjudicated or that a patient-specific medical conclusion was reached.

Non-clinical example: A reviewer rejects a draft because it repeatedly gives patient-facing instructions and cannot be converted into a bounded review artifact without replacement.

## escalated

Workflow meaning: A higher-level human review path is needed before the packet can proceed.

When it may be used: Use `escalated` when the draft contains sensitive, ambiguous, unsupported, or boundary-adjacent language that requires additional workflow review.

What it does not mean: It does not mean the patient has high medical risk or that clinical urgency has been determined.

Non-clinical example: A reviewer escalates a packet because the draft includes unsupported urgency language and the source context is incomplete.

## pending

Workflow meaning: No final workflow decision has been recorded yet.

When it may be used: Use `pending` before reviewer workflow assessment is complete.

What it does not mean: It does not mean the AI output is acceptable, clinically correct, medically unsafe, or clinically unresolved.

Non-clinical example: A packet remains pending while a reviewer checks whether source evidence links and missing-information flags are complete.

## What Reviewer Decisions Are Not

Reviewer decisions are not:

- diagnoses
- treatment recommendations
- clinical correctness validations
- medical safety assessments
- patient-facing advice
- clinician replacement
- compliance guarantees

## Current Synthetic Examples

Case 001 uses a reviewer decision to demonstrate revision need due to healthcare-adjacent interpretation and missing context.

Case 002 uses a reviewer decision to demonstrate revision or escalation need due to unsupported or over-specific AI output under incomplete source context.

Both examples are synthetic and non-clinical. Their reviewer decisions are workflow metadata only.

