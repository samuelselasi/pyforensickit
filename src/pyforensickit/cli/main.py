import argparse
from rich.console import Console
from rich.panel import Panel
from rich.pretty import Pretty
from pyforensickit.core.hashing import compute_hashes
from pyforensickit.core.metadata import extract_metadata
from pyforensickit.core.timeline import build_timeline

console = Console()

def analyze(path, output, timeline_csv=None):
    console.print(Panel.fit(
        f"[bold]PyForensicKit[/bold]\nAnalyzing: {path}",
        title="Digital Forensics Toolkit"
    ))

    hashes = compute_hashes(path)
    metadata = extract_metadata(path)
    timeline = build_timeline(path)

    console.print("\n[bold green]Timeline (first 10 events)[/bold green]")
    for event in timeline[:10]:
        console.print(event)

    console.print("\n[bold green]Metadata[/bold green]")
    for k, v in metadata.items():
        console.print(f"{k}: {v}")

    console.print("\n[bold green]Hashes[/bold green]")
    console.print(Pretty(hashes))

    if output:
        import json
        with open(output, "w") as f:
            json.dump(
                    {"metadata": metadata, "hashes": hashes, "timeline": timeline},
                f,
                indent=4
            )
        console.print(f"\n[yellow]Report saved to {output}[/yellow]")

    if timeline_csv:
        from pyforensickit.core.timeline import export_timeline_csv
        export_timeline_csv(timeline, timeline_csv)
        console.print(
            f"[yellow]Timeline exported to {timeline_csv}[/yellow]"
        )


def main():
    parser = argparse.ArgumentParser(
        description="PyForensicKit – Digital Forensics CLI Toolkit"
    )

    parser.add_argument(
        "path",
        help="Path to evidence file or directory"
    )

    parser.add_argument(
        "-o", "--output",
        help="Save forensic report to JSON file"
    )

    parser.add_argument(
        "--timeline-csv",
        help="Export timeline to CSV file"
    )

    args = parser.parse_args()
    analyze(args.path, args.output, args.timeline_csv)

if __name__ == "__main__":
    main()
