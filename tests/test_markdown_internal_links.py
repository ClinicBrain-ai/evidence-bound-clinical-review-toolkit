import re
from pathlib import Path


MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
IGNORED_PREFIXES = ("http://", "https://", "mailto:")


def markdown_files(repo_root):
    paths = [
        repo_root / "README.md",
        repo_root / "CONTRIBUTING.md",
        repo_root / "CHANGELOG.md",
    ]
    paths.extend(sorted((repo_root / "docs").glob("*.md")))
    paths.extend(sorted((repo_root / "examples").glob("**/*.md")))
    return paths


def normalize_link_target(raw_target):
    target = raw_target.strip()

    if not target:
        return None

    if target.startswith(IGNORED_PREFIXES) or target.startswith("#"):
        return None

    target = target.split("#", 1)[0]
    return target.strip()


def test_internal_markdown_links_point_to_existing_targets():
    repo_root = Path(__file__).resolve().parents[1]
    broken_links = []

    for markdown_path in markdown_files(repo_root):
        text = markdown_path.read_text(encoding="utf-8")

        for match in MARKDOWN_LINK_PATTERN.finditer(text):
            target = normalize_link_target(match.group(1))

            if target is None:
                continue

            resolved_target = (markdown_path.parent / target).resolve()

            if not resolved_target.exists():
                broken_links.append(
                    f"{markdown_path.relative_to(repo_root)} -> {match.group(1)}"
                )

    assert not broken_links, "Broken internal Markdown links:\n" + "\n".join(
        broken_links
    )

