import argparse
from pyforensickit.core.hashing import compute_hashes
from pyforensickit.core.metadata import extract_metadata
from rich.console import Console

console = Console()

def analyze(path, output=None):
    console.print("[bold cyan]Analyzing evidence...[/bold cyan]")

    hashes = compute_hashes(path)
    metadata = extract_metadata(path)

    console.print("[green]Hashes:[/green]", hashes)
    console.print("[green]Metadata:[/green]", metadata)

    if output:
        import json
        with open(output, "w") as f:
            json.dump(
                {"hashes": hashes, "metadata": metadata},
                f,
                indent=4
            )
        console.print(f"[yellow]Report saved to {output}[/yellow]")

def main():
    parser = argparse.ArgumentParser(
        description="PyForensicKit - Digital Forensics Toolkit"
    )

    parser.add_argument(
        "path",
        help="Path to file or directory to analyze"
    )

    parser.add_argument(
        "--output",
        help="Save analysis report to file"
    )

    args = parser.parse_args()
    analyze(args.path, args.output)

if __name__ == "__main__":
    main()
