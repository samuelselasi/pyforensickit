import tempfile
from pyforensickit.core.hashing import compute_hashes, verify_integrity


def test_compute_hashes_single_file():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"forensic test data")
        path = f.name

    hashes = compute_hashes(path)

    # compute_hashes hashes ONE file and returns a flat dict
    assert isinstance(hashes, dict)
    assert "md5" in hashes
    assert "sha1" in hashes
    assert "sha256" in hashes

    # values should be non-empty strings
    assert isinstance(hashes["md5"], str)
    assert isinstance(hashes["sha1"], str)
    assert isinstance(hashes["sha256"], str)

def test_verify_integrity_passes():
    import tempfile
    from pyforensickit.core.hashing import verify_integrity
    import os

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"integrity check")
        path = f.name

    result = verify_integrity(path)

    # verify_integrity returns a forensic integrity report
    assert isinstance(result, dict)
    assert "original" in result
    assert "after_analysis" in result
    assert "integrity_pass" in result

    # Get the file key
    file_key = path

    # each stage should contain hashes
    for section in ("original", "after_analysis"):
        assert "md5" in result[section][file_key]
        assert "sha1" in result[section][file_key]
        assert "sha256" in result[section][file_key]

    # integrity verification should pass for unchanged file
    assert result["integrity_pass"][file_key] is True
