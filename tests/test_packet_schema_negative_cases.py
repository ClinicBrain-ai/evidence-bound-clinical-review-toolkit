import copy
import json
from pathlib import Path

import pytest
from jsonschema import ValidationError, validate


def load_schema_and_packet():
    repo_root = Path(__file__).resolve().parents[1]
    schema_path = repo_root / "schemas" / "clinical_review_packet.schema.json"
    packet_path = (
        repo_root
        / "examples"
        / "synthetic_dental_case_001"
        / "clinical_review_packet.json"
    )

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    packet = json.loads(packet_path.read_text(encoding="utf-8"))
    return schema, packet


def assert_invalid_packet(packet):
    schema, _ = load_schema_and_packet()

    with pytest.raises(ValidationError):
        validate(instance=packet, schema=schema)


def test_rejects_missing_original_ai_output_text():
    _, packet = load_schema_and_packet()
    invalid_packet = copy.deepcopy(packet)
    invalid_packet["original_ai_output"].pop("text")

    assert_invalid_packet(invalid_packet)


def test_rejects_empty_source_evidence():
    _, packet = load_schema_and_packet()
    invalid_packet = copy.deepcopy(packet)
    invalid_packet["source_evidence"] = []

    assert_invalid_packet(invalid_packet)


def test_rejects_source_evidence_item_missing_excerpt():
    _, packet = load_schema_and_packet()
    invalid_packet = copy.deepcopy(packet)
    invalid_packet["source_evidence"][0].pop("excerpt")

    assert_invalid_packet(invalid_packet)


def test_rejects_invalid_missing_information_status():
    _, packet = load_schema_and_packet()
    invalid_packet = copy.deepcopy(packet)
    invalid_packet["missing_information"][0]["status"] = "unclear_clinical_status"

    assert_invalid_packet(invalid_packet)


def test_rejects_invalid_workflow_risk_level():
    _, packet = load_schema_and_packet()
    invalid_packet = copy.deepcopy(packet)
    invalid_packet["risk_assessment"]["risk_level"] = "severe_clinical_risk"

    assert_invalid_packet(invalid_packet)


def test_rejects_missing_human_review_required():
    _, packet = load_schema_and_packet()
    invalid_packet = copy.deepcopy(packet)
    invalid_packet["review_requirement"].pop("human_review_required")

    assert_invalid_packet(invalid_packet)


def test_rejects_invalid_reviewer_decision():
    _, packet = load_schema_and_packet()
    invalid_packet = copy.deepcopy(packet)
    invalid_packet["review_status"]["decision"] = "clinically_validated"

    assert_invalid_packet(invalid_packet)


def test_rejects_empty_audit_events():
    _, packet = load_schema_and_packet()
    invalid_packet = copy.deepcopy(packet)
    invalid_packet["audit_events"] = []

    assert_invalid_packet(invalid_packet)

