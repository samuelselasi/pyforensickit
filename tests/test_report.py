import tempfile
import os
from pyforensickit.core.report import generate_report

def test_generate_html_report():
    with tempfile.TemporaryDirectory() as tmpdir:
        html_path = os.path.join(tmpdir, "report.html")

        generate_report(
            output_html=html_path,
            case={"case_id": "CASE-TEST"},
            metadata={"path": "/test"},
            hashes={"file": {"md5": "abc"}},
            timeline=[],
            integrity_verification={}
        )

        assert os.path.exists(html_path)
        assert os.path.getsize(html_path) > 0
