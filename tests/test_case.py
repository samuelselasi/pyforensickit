from pyforensickit.core.case import ForensicCase

def test_forensic_case_to_dict():
    case = ForensicCase(
        case_id="CASE-001",
        investigator="Jane Doe",
        description="Test case"
    )

    data = case.to_dict()

    assert data["case_id"] == "CASE-001"
    assert data["investigator"] == "Jane Doe"
    assert data["description"] == "Test case"
    assert "analysis_started_utc" in data
