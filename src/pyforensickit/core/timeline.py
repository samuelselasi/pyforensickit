from pathlib import Path
from datetime import datetime
import csv

def build_timeline(path):
    path = Path(path)
    events = []

    if path.is_file():
        _add_file_events(path, events)
    elif path.is_dir():
        for file in path.rglob("*"):
            if file.is_file():
                _add_file_events(file, events)
    else:
        raise ValueError("Invalid evidence path")

    events.sort(key=lambda x: x["timestamp"])
    return events

def _add_file_events(file_path, events):
    try:
        stat = file_path.stat()
    except PermissionError:
        return

    events.extend([
        _event("created", file_path, stat.st_ctime),
        _event("modified", file_path, stat.st_mtime),
        _event("accessed", file_path, stat.st_atime),
    ])

def _event(event_type, path, ts):
    return {
        "event": event_type,
        "path": str(path),
        "timestamp": datetime.fromtimestamp(ts).isoformat()
    }

def export_timeline_csv(timeline, output_file):
    fieldnames = ["event", "path", "timestamp"]

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(timeline)
