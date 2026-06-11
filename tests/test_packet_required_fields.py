import json
from pathlib import Path


REQUIRED_FIELDS = {
    "packet_id",
    "case_type",
    "ai_output_type",
    "original_ai_output",
    "source_evidence",
    "missing_information",
    "risk_assessment",
    "review_requirement",
    "review_status",
    "audit_events",
}


def test_example_packet_includes_required_top_level_fields():
    repo_root = Path(__file__).resolve().parents[1]
    packet_path = (
        repo_root
        / "examples"
        / "synthetic_dental_case_001"
        / "clinical_review_packet.json"
    )

    packet = json.loads(packet_path.read_text(encoding="utf-8"))

    assert REQUIRED_FIELDS.issubset(packet.keys())

