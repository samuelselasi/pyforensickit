import hashlib
from pathlib import Path

SUPPORTED_HASHES = ("md5", "sha1", "sha256")


def compute_hashes(path):
    """
    Compute cryptographic hashes for a file or directory.

    - File → returns {hash_name: digest}
    - Directory → returns {file_path: {hash_name: digest}}
    """
    path = Path(path)

    if path.is_file():
        return _safe_hash_file(path)

    if path.is_dir():
        results = {}
        for file in path.rglob("*"):
            if file.is_file():
                results[str(file)] = _safe_hash_file(file)
        return results

    raise ValueError(f"Evidence path does not exist or is not accessible: {path}")


def _safe_hash_file(file_path):
    try:
        return _hash_file(file_path)
    except PermissionError:
        return {"error": "permission denied"}
    except OSError as e:
        return {"error": str(e)}


def _hash_file(file_path):
    hashers = {name: hashlib.new(name) for name in SUPPORTED_HASHES}

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            for h in hashers.values():
                h.update(chunk)

    return {name: h.hexdigest() for name, h in hashers.items()}


def verify_integrity(path):
    """
    Compute hashes before and after analysis and verify immutability.
    Returns a dict:
    {
        "original": {file: hashes},
        "after_analysis": {file: hashes},
        "integrity_pass": {file: True/False}
    }
    """
    from pathlib import Path
    from .hashing import compute_hashes  # assuming same module

    path_obj = Path(path)

    # Ensure we always get a path-keyed dict
    original_hashes = compute_hashes(path)
    if path_obj.is_file():
        original = {str(path_obj): original_hashes}
    else:
        original = original_hashes

    after_hashes = compute_hashes(path)
    if path_obj.is_file():
        after = {str(path_obj): after_hashes}
    else:
        after = after_hashes

    integrity_pass = {}
    for f in original:
        if isinstance(original[f], dict) and "error" not in original[f]:
            integrity_pass[f] = original[f] == after.get(f, {})
        else:
            integrity_pass[f] = None

    return {
        "original": original,
        "after_analysis": after,
        "integrity_pass": integrity_pass
    }
