import argparse
import json
from rich.console import Console
from rich.panel import Panel
from rich.pretty import Pretty

from pyforensickit.core.hashing import compute_hashes, verify_integrity
from pyforensickit.core.metadata import extract_metadata
from pyforensickit.core.timeline import build_timeline, export_timeline_csv
from pyforensickit.core.case import ForensicCase
from pyforensickit.core.report import generate_report

console = Console()


def analyze(
    path,
    output=None,
    timeline_csv=None,
    case=None,
    verify_integrity_flag=False,
    report_html=None,
    report_pdf=None,
):
    """
    Perform forensic analysis on a file or directory.
    """

    # ---- Case Information ----
    if case:
        console.print("\n[bold cyan]Case Information[/bold cyan]")
        for k, v in case.to_dict().items():
            console.print(f"{k}: {v}")

    console.print(
        Panel.fit(
            f"[bold]PyForensicKit[/bold]\nAnalyzing: {path}",
            title="Digital Forensics Toolkit",
        )
    )

    # ---- Integrity Verification ----
    integrity_result = None
    if verify_integrity_flag:
        console.print("\n[bold blue]Verifying evidence integrity (read-only)...[/bold blue]")
        integrity_result = verify_integrity(path)

        passed = sum(v is True for v in integrity_result["integrity_pass"].values())
        failed = sum(v is False for v in integrity_result["integrity_pass"].values())
        unknown = sum(v is None for v in integrity_result["integrity_pass"].values())

        console.print(
            f"[green]Integrity verification complete[/green] "
            f"(passed={passed}, failed={failed}, unknown={unknown})"
        )

    # ---- Core Analysis ----
    hashes = compute_hashes(path)
    metadata = extract_metadata(path)
    timeline = build_timeline(path)

    # ---- Terminal Output ----
    console.print("\n[bold green]Timeline (first 10 events)[/bold green]")
    for event in timeline[:10]:
        console.print(event)

    console.print("\n[bold green]Metadata[/bold green]")
    for k, v in metadata.items():
        console.print(f"{k}: {v}")

    console.print("\n[bold green]Hashes[/bold green]")
    console.print(Pretty(hashes))

    # ---- JSON Report ----
    if output:
        with open(output, "w") as f:
            json.dump(
                {
                    "case": case.to_dict() if case else None,
                    "metadata": metadata,
                    "hashes": hashes,
                    "timeline": timeline,
                    "integrity_verification": integrity_result,
                },
                f,
                indent=4,
            )
        console.print(f"\n[yellow]JSON report saved to {output}[/yellow]")

    # ---- Timeline CSV ----
    if timeline_csv:
        export_timeline_csv(timeline, timeline_csv)
        console.print(f"[yellow]Timeline exported to {timeline_csv}[/yellow]")

    # ---- HTML / PDF Report ----
    if report_html:
        generate_report(
            output_html=report_html,
            output_pdf=report_pdf,
            case=case.to_dict() if case else None,
            metadata=metadata,
            hashes=hashes,
            timeline=timeline,
            integrity_verification=integrity_result,
        )
        console.print(f"[yellow]HTML report generated at {report_html}[/yellow]")
        if report_pdf:
            console.print(f"[yellow]PDF report generated at {report_pdf}[/yellow]")


def main():
    parser = argparse.ArgumentParser(
        description="PyForensicKit – Digital Forensics CLI Toolkit"
    )

    parser.add_argument(
        "path",
        help="Path to evidence file or directory",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Save forensic report to JSON file",
    )

    parser.add_argument(
        "--timeline-csv",
        help="Export timeline to CSV file",
    )

    parser.add_argument(
        "--case-id",
        help="Forensic case identifier",
    )

    parser.add_argument(
        "--investigator",
        help="Investigator name",
    )

    parser.add_argument(
        "--description",
        help="Brief case description",
    )

    parser.add_argument(
        "--verify-integrity",
        action="store_true",
        help="Verify evidence integrity before and after analysis",
    )

    parser.add_argument(
        "--report-html",
        help="Output HTML report path",
    )

    parser.add_argument(
        "--report-pdf",
        help="Output PDF report path",
    )

    args = parser.parse_args()

    # ---- Case Object ----
    case = ForensicCase(
        case_id=args.case_id,
        investigator=args.investigator,
        description=args.description,
    )

    # ---- Run Analysis ----
    analyze(
        path=args.path,
        output=args.output,
        timeline_csv=args.timeline_csv,
        case=case,
        verify_integrity_flag=args.verify_integrity,
        report_html=args.report_html,
        report_pdf=args.report_pdf,
    )


if __name__ == "__main__":
    main()
