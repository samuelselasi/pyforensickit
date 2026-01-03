import hashlib
from pathlib import Path

def compute_hashes(path):
    path = Path(path)

    if path.is_file():
        return _hash_file(path)
    elif path.is_dir():
        return {
            str(p): _hash_file(p)
            for p in path.rglob("*")
            if p.is_file()
        }
    else:
        raise ValueError("Invalid path")

def _hash_file(file_path):
    hashes = {
        "md5": hashlib.md5(),
        "sha1": hashlib.sha1(),
        "sha256": hashlib.sha256()
    }

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            for h in hashes.values():
                h.update(chunk)

    return {name: h.hexdigest() for name, h in hashes.items()}
