import hashlib
from pathlib import Path

SUPPORTED_HASHES = ("md5", "sha1", "sha256")

def compute_hashes(path):
    path = Path(path)

    if path.is_file():
        return _hash_file(path)

    if path.is_dir():
        results = {}
        for file in path.rglob("*"):
            if file.is_file():
                results[str(file)] = _hash_file(file)
        return results

    raise ValueError("Invalid evidence path")

def _hash_file(file_path):
    hashers = {
        name: hashlib.new(name)
        for name in SUPPORTED_HASHES
    }

    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            for h in hashers.values():
                h.update(chunk)

    return {name: h.hexdigest() for name, h in hashers.items()}
