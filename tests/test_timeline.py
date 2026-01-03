import tempfile
import os
from pyforensickit.core.timeline import build_timeline

def test_build_timeline_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "file.txt")
        with open(file_path, "w") as f:
            f.write("timeline test")

        timeline = build_timeline(tmpdir)

        assert isinstance(timeline, list)
        assert len(timeline) > 0
        assert "path" in timeline[0]
        assert "event" in timeline[0]
        assert "timestamp" in timeline[0]
