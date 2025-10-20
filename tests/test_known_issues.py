import json
from pathlib import Path


def test_known_issues_have_title_and_description():
    data_path = Path(__file__).resolve().parent.parent / 'known-issues.json'
    with data_path.open() as f:
        data = json.load(f)

    issues = data.get('issues', [])
    assert isinstance(issues, list), "'issues' should be a list"

    for issue in issues:
        assert 'title' in issue, "Issue missing 'title' key"
        assert 'description' in issue, "Issue missing 'description' key"

