import os
import stat
from pathlib import Path
from datetime import datetime

def extract_metadata(path):
    path = Path(path)
    stat_info = path.stat()

    return {
        "path": str(path),
        "size_bytes": stat_info.st_size,
        "permissions": stat.filemode(stat_info.st_mode),
        "owner_uid": stat_info.st_uid,
        "group_gid": stat_info.st_gid,
        "created": _format_time(stat_info.st_ctime),
        "modified": _format_time(stat_info.st_mtime),
        "accessed": _format_time(stat_info.st_atime)
    }

def _format_time(ts):
    return datetime.fromtimestamp(ts).isoformat()
