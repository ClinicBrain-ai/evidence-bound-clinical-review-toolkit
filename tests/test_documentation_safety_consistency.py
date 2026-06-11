from pathlib import Path


REQUIRED_DOCUMENT_TERMS = {
    "README.md": [
        "review infrastructure",
        "diagnosis",
        "treatment",
        "clinical correctness",
        "real patient",
        "clinical deployment",
        "hipaa",
        "medical device",
    ],
    "CONTRIBUTING.md": [
        "review infrastructure",
        "diagnosis",
        "treatment",
        "clinical correctness",
        "real patient",
        "production readiness",
        "hipaa",
        "medical-device functionality",
    ],
    "docs/SCHEMA_FIELD_REFERENCE.md": [
        "workflow metadata",
        "clinical correctness",
        "diagnosis",
        "treatment",
        "real patient",
        "production readiness",
        "hipaa compliance",
        "medical-device functionality",
    ],
}


def test_core_safety_boundary_language_remains_present():
    repo_root = Path(__file__).resolve().parents[1]

    for relative_path, required_terms in REQUIRED_DOCUMENT_TERMS.items():
        document_path = repo_root / relative_path

        assert document_path.exists(), f"Missing required document: {relative_path}"

        document_text = document_path.read_text(encoding="utf-8").lower()
        missing_terms = [
            term for term in required_terms if term.lower() not in document_text
        ]

        assert not missing_terms, (
            f"{relative_path} is missing safety-boundary terms: "
            f"{', '.join(missing_terms)}"
        )

