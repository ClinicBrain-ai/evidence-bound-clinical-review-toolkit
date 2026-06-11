# Review Packet Lifecycle

This document explains Clinical Review Packet lifecycle states as workflow metadata.

The lifecycle does not represent patient clinical status, diagnosis progression, treatment planning, clinical severity scoring, medical safety validation, patient-facing guidance, production clinical workflow deployment, or legal or HIPAA compliance guarantees.

## Lifecycle Diagram

```text
AI-generated draft
  -> Clinical Review Packet created
  -> Evidence and missing context recorded
  -> Workflow risk label assigned
  -> Human review decision
  -> Audit event recorded
  -> Packet outcome
```

## Workflow States

1. AI draft created

   An AI-generated healthcare-adjacent draft exists as unverified text.

2. Packet created

   The draft is placed into a structured Clinical Review Packet.

3. Evidence mapped

   Available source material is linked to packet statements for traceability.

4. Missing information recorded

   Absent or unknown context is made visible for reviewer attention.

5. Workflow risk label assigned

   A routing label is assigned for workflow attention. This is not a clinical severity score.

6. Human review required or not required

   The packet records whether human review is required in the prototype workflow.

7. Reviewer decision recorded

   A reviewer workflow decision is captured.

8. Audit event appended

   A workflow event is recorded for packet history.

9. Packet closed, revised, rejected, or escalated

   The packet reaches a workflow outcome.

## Packet Outcomes

- `approved`: The packet is approved for the intended non-clinical workflow context.
- `requires_revision`: The packet requires edits before downstream workflow use.
- `rejected`: The packet should not proceed in the workflow.
- `escalated`: The packet requires additional review attention.
- `pending`: The packet has not reached a final workflow decision.

These outcomes are workflow outcomes. They are not proof of clinical correctness, diagnostic accuracy, treatment safety, or medical appropriateness.

## Field Relationships

- `original_ai_output` captures the AI-generated draft.
- `source_evidence` links packet claims to provided source material.
- `missing_information` records absent or unknown context.
- `risk_assessment.risk_level` routes workflow attention.
- `review_requirement` records whether human review is required.
- `review_status` records reviewer workflow decision.
- `audit_events` preserve the packet history.

## What This Lifecycle Does Not Represent

This lifecycle does not represent:

- patient clinical status
- diagnosis progression
- treatment planning
- clinical severity scoring
- medical safety validation
- patient-facing guidance
- production clinical workflow deployment
- legal or HIPAA compliance guarantee

