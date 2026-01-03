import argparse
from rich.console import Console
from rich.panel import Panel
from pyforensickit.core.hashing import compute_hashes
from pyforensickit.core.metadata import extract_metadata

console = Console()

def analyze(path, output):
    console.print(Panel.fit(
        f"[bold]PyForensicKit[/bold]\nAnalyzing: {path}",
        title="Digital Forensics Toolkit"
    ))

    hashes = compute_hashes(path)
    metadata = extract_metadata(path)

    console.print("\n[bold green]Metadata[/bold green]")
    for k, v in metadata.items():
        console.print(f"{k}: {v}")

    console.print("\n[bold green]Hashes[/bold green]")
    console.print(hashes)

    if output:
        import json
        with open(output, "w") as f:
            json.dump(
                {"metadata": metadata, "hashes": hashes},
                f,
                indent=4
            )
        console.print(f"\n[yellow]Report saved to {output}[/yellow]")

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

    args = parser.parse_args()
    analyze(args.path, args.output)

if __name__ == "__main__":
    main()
