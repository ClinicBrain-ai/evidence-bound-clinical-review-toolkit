# Synthetic Dental Case 003 Walkthrough

This walkthrough explains the third synthetic example as a reviewability artifact, not a clinical assessment.

The packet does not resolve the clinical conflict. It preserves the conflict so a human reviewer can see what each source says, what the AI draft over-smooths or overstates, what information is missing, why human review is required, what workflow decision was recorded, and what audit trail was preserved.

## 1. Input Case Summary

The input summary is fictional and de-identified. It contains two source notes with differing descriptions.

Source note A says an adult reports discomfort around a lower left tooth area after a recent dental visit, most noticeable when chewing.

Source note B says the person later described symptoms as improving and "not clearly in one spot."

The timing between the notes is unclear, and key context is absent.

## 2. AI-Generated Draft Output

The AI draft presents the situation as improving lower left post-visit discomfort and says no distinct concern is apparent from the available information.

That draft is too confident because it smooths over the difference between source note A and source note B.

## 3. Why the AI Output Requires Review

The draft requires review because it turns conflicting source information into a more unified narrative than the source supports.

The review process does not decide which source note is clinically correct. It identifies that the conflict should remain visible in the packet.

## 4. How source_evidence Preserves the Conflict

The `source_evidence` array records what each source actually says:

- source note A reports lower left tooth-area discomfort after a recent dental visit
- source note A reports discomfort most noticeable when chewing
- source note B reports symptoms as improving and not clearly localized
- the timing between notes is unclear

This supports traceability. It does not resolve the source conflict or prove medical correctness.

## 5. How missing_information Records Absent or Unclear Context

The `missing_information` array records missing or unknown context, including visit date, procedure details, timing between source notes, recent imaging, medication history, allergy information, clinician exam findings, and explanation for differing symptom descriptions.

These fields are workflow prompts. They are not diagnoses, treatment gaps, clinical findings, or medical safety determinations.

## 6. How risk_assessment.risk_level Functions as Workflow Routing Metadata

The packet assigns `risk_assessment.risk_level` as `medium`.

This is a workflow routing label because the draft smooths over conflicting source information under incomplete context.

The label is not a clinical severity score, patient risk score, diagnosis, or clinical triage decision.

## 7. Why review_requirement.human_review_required Is True

The packet sets `review_requirement.human_review_required` to `true` because the AI draft does not preserve the conflicting source descriptions.

This field is a workflow control, not a patient-care instruction.

## 8. How review_status.decision Captures a Reviewer Workflow Decision

The packet records `review_status.decision` as `escalated`.

This means a higher-level workflow review path is needed before the packet can proceed.

The decision is not proof of clinical correctness, diagnostic accuracy, medical severity, treatment safety, or patient-specific risk.

## 9. How audit_events Preserve Workflow History

The `audit_events` array records packet creation and human review recording.

These events support prototype traceability. They are not legal compliance guarantees, HIPAA compliance guarantees, production readiness evidence, or medical-device audit records.

## What This Walkthrough Does Not Do

This walkthrough does not:

- diagnose the patient
- recommend treatment
- validate clinical correctness
- assess medical safety
- provide patient advice
- replace a clinician or licensed reviewer
- resolve the source conflict

