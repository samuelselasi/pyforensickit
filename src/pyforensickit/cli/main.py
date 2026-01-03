import argparse
from rich.console import Console
from rich.panel import Panel
from rich.pretty import Pretty
from pyforensickit.core.hashing import compute_hashes
from pyforensickit.core.metadata import extract_metadata
from pyforensickit.core.timeline import build_timeline
from pyforensickit.core.case import ForensicCase
from pyforensickit.core.hashing import verify_integrity

console = Console()

def analyze(path, output, timeline_csv=None, case=None):
    if case:
        console.print("\n[bold cyan]Case Information[/bold cyan]")
        for k, v in case.to_dict().items():
            console.print(f"{k}: {v}")

    console.print(Panel.fit(
        f"[bold]PyForensicKit[/bold]\nAnalyzing: {path}",
        title="Digital Forensics Toolkit"
    ))

    if verify_integrity:
        integrity_result = verify_integrity(path)
    else:
        integrity_result = None

    console.print("\n[bold blue]Verifying evidence integrity...[/bold blue]")
    integrity_result = verify_integrity(path)
    console.print("[green]Integrity verification complete[/green]")

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
                    {"case": case.to_dict() if case else NOne, "metadata": metadata, "hashes": hashes, "timeline": timeline, "integrity_verification": integrity_result},
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

    parser.add_argument(
        "--case-id",
        help="Forensic case identifier"
    )

    parser.add_argument(
        "--investigator",
        help="Investigator name"
    )

    parser.add_argument(
        "--description",
        help="Brief case description"
    )

    parser.add_argument(
        "--verify-integrity",
        action="store_true",
        help="Verify evidence integrity before and after analysis"
    )

    args = parser.parse_args()

    case = ForensicCase(
            case_id=args.case_id,
            investigator=args.investigator,
            description=args.description
    )

    # args = parser.parse_args()
    analyze(args.path, args.output, args.timeline_csv, case)

if __name__ == "__main__":
    main()
