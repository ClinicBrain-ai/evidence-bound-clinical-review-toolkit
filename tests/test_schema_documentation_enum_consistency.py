import json
from pathlib import Path


EXPECTED_DECISION_VALUES = {
    "approved",
    "requires_revision",
    "rejected",
    "escalated",
    "pending",
}

EXPECTED_RISK_LEVEL_VALUES = {
    "low",
    "medium",
    "high",
}

EXPECTED_MISSING_INFORMATION_STATUS_VALUES = {
    "missing",
    "present",
    "unknown",
    "not_applicable",
}


def test_review_decision_schema_enum_is_documented():
    repo_root = Path(__file__).resolve().parents[1]
    schema_path = repo_root / "schemas" / "clinical_review_packet.schema.json"
    guide_path = repo_root / "docs" / "REVIEW_DECISION_GUIDE.md"

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    guide_text = guide_path.read_text(encoding="utf-8").lower()

    decision_values = set(
        schema["properties"]["review_status"]["properties"]["decision"]["enum"]
    )

    assert decision_values == EXPECTED_DECISION_VALUES

    missing_values = [
        value for value in sorted(decision_values) if value not in guide_text
    ]

    assert not missing_values, (
        "Review decision enum values missing from docs/REVIEW_DECISION_GUIDE.md: "
        + ", ".join(missing_values)
    )


def test_risk_level_schema_enum_is_documented():
    repo_root = Path(__file__).resolve().parents[1]
    schema_path = repo_root / "schemas" / "clinical_review_packet.schema.json"
    field_reference_path = repo_root / "docs" / "SCHEMA_FIELD_REFERENCE.md"

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    field_reference_text = field_reference_path.read_text(encoding="utf-8").lower()

    risk_level_values = set(
        schema["properties"]["risk_assessment"]["properties"]["risk_level"]["enum"]
    )

    assert risk_level_values == EXPECTED_RISK_LEVEL_VALUES

    missing_values = [
        value for value in sorted(risk_level_values) if value not in field_reference_text
    ]

    assert not missing_values, (
        "Risk level enum values missing from docs/SCHEMA_FIELD_REFERENCE.md: "
        + ", ".join(missing_values)
    )


def test_missing_information_status_schema_enum_is_documented():
    repo_root = Path(__file__).resolve().parents[1]
    schema_path = repo_root / "schemas" / "clinical_review_packet.schema.json"
    field_reference_path = repo_root / "docs" / "SCHEMA_FIELD_REFERENCE.md"

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    field_reference_text = field_reference_path.read_text(encoding="utf-8").lower()

    status_values = set(
        schema["properties"]["missing_information"]["items"]["properties"]["status"][
            "enum"
        ]
    )

    assert status_values == EXPECTED_MISSING_INFORMATION_STATUS_VALUES

    missing_values = [
        value for value in sorted(status_values) if value not in field_reference_text
    ]

    assert not missing_values, (
        "Missing-information status enum values missing from "
        "docs/SCHEMA_FIELD_REFERENCE.md: "
        + ", ".join(missing_values)
    )
