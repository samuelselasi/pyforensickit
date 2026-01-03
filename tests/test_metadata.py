import tempfile
from pyforensickit.core.metadata import extract_metadata

def test_extract_metadata_file():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"metadata test")
        path = f.name

    metadata = extract_metadata(path)

    assert metadata["path"] == path
    assert metadata["size_bytes"] > 0
    assert "permissions" in metadata
    assert "modified" in metadata
