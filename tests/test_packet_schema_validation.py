import json
from pathlib import Path

import pytest
from jsonschema import validate


def example_packet_paths():
    repo_root = Path(__file__).resolve().parents[1]
    return sorted((repo_root / "examples").glob("**/clinical_review_packet.json"))


@pytest.mark.parametrize("packet_path", example_packet_paths())
def test_example_packets_conform_to_clinical_review_packet_schema(packet_path):
    repo_root = Path(__file__).resolve().parents[1]
    schema_path = repo_root / "schemas" / "clinical_review_packet.schema.json"

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    packet = json.loads(packet_path.read_text(encoding="utf-8"))

    validate(instance=packet, schema=schema)
