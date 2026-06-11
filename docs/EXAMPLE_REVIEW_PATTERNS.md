# Example Review Patterns

The examples in this repository are synthetic and designed to demonstrate reviewability patterns, not clinical assessment.

Each example shows how an AI-generated healthcare-adjacent draft can be converted into a Clinical Review Packet that makes source support, missing context, workflow routing, reviewer decisions, and audit history easier to inspect.

| Example | Pattern Demonstrated | AI Draft Problem | What the Packet Makes Reviewable | What the Packet Does Not Decide |
| --- | --- | --- | --- | --- |
| [Case 001](../examples/synthetic_dental_case_001/) | Missing context | The draft references possible infection or inflammation while important context is absent. | Missing imaging, medication history, allergy information, periodontal assessment, and related review context. | It does not diagnose, recommend treatment, or determine medical severity. |
| [Case 002](../examples/synthetic_dental_case_002/) | Unsupported or over-specific AI output | The draft sounds fluent but becomes too specific relative to the provided source material. | Source-supported details, missing procedure context, and unsupported specificity that needs human review. | It does not decide whether the AI output is clinically correct. |
| [Case 003](../examples/synthetic_dental_case_003/) | Conflicting source information | The draft smooths over differing source descriptions and presents the situation too confidently. | What each source says, what is missing, what the draft overstates, and why escalation was recorded. | It does not resolve the clinical conflict. |

## Case 001: Missing Context

Case 001 demonstrates how absent information such as imaging, medication history, allergy information, or assessment context can be recorded as missing-information workflow metadata.

Boundary: The packet does not diagnose, recommend treatment, or determine medical severity.

## Case 002: Unsupported or Over-Specific AI Output

Case 002 demonstrates how an AI-generated draft may sound fluent but become too specific relative to the provided source material.

Boundary: The packet does not decide whether the AI output is clinically correct. It makes unsupported specificity visible for human review.

## Case 003: Conflicting Source Information

Case 003 demonstrates how differing source descriptions can be preserved rather than smoothed over by the AI draft.

Boundary: The packet does not resolve the clinical conflict. It makes the conflict visible for human review.

## Why Multiple Examples Matter

Multiple synthetic examples show that the toolkit is not just a single JSON demo. The same Clinical Review Packet structure can represent different review situations:

- missing context
- unsupported specificity
- conflicting source information

The repeatability is in the review structure, not in any clinical conclusion.

## What These Examples Do Not Demonstrate

These examples do not demonstrate:

- diagnosis
- treatment recommendation
- clinical correctness validation
- medical safety assessment
- patient-facing advice
- clinician replacement
- real clinical deployment
- HIPAA compliance
- medical-device functionality

