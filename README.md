# PyForensicKit

> **PyForensicKit** is a Linux-based digital forensics command-line toolkit designed to assist investigators in analyzing digital evidence while preserving forensic integrity.

## Features

- Cryptographic hashing (MD5, SHA1, SHA256)
- File metadata extraction
- Read-only evidence analysis
- JSON, HTML, and PDF report generation
- Modular and extensible architecture
- File system timeline reconstruction
- CSV and JSON timeline export
- Evidence integrity verification
- Case management support

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/samuelselasi/pyforensickit.git
cd pyforensickit
pip install -r requirements.txt
```

> **Note:** `libmagic` is required for full metadata extraction. On Ubuntu, install with:

```bash
sudo apt-get update
sudo apt-get install -y libmagic1
```

## Usage

### Basic JSON Report

Analyze evidence and save a JSON report:

```bash
python -m pyforensickit.cli.main /path/to/evidence --output report.json
```

### Timeline CSV Export

Analyze and export file timeline as CSV:

```bash
python -m pyforensickit.cli.main /path/to/evidence --timeline-csv timeline.csv
```

### Full Report with Integrity Verification

Generate JSON, HTML, and PDF reports while verifying evidence integrity:

```bash
python -m pyforensickit.cli.main /path/to/evidence \
    --output report.json \
    --report-html report.html \
    --report-pdf report.pdf \
    --verify-integrity \
    --case-id CASE-2026-01 \
    --investigator "John Doe" \
    --description "Baseline system analysis"
```

### CLI Options

| Option                     | Description                                               |
|-----------------------------|-----------------------------------------------------------|
| `path`                      | Path to evidence file or directory                        |
| `-o`, `--output`            | Save forensic report to JSON file                         |
| `--timeline-csv`            | Export timeline to CSV file                                |
| `--case-id`                 | Forensic case identifier                                   |
| `--investigator`            | Investigator name                                         |
| `--description`             | Brief case description                                     |
| `--verify-integrity`        | Verify evidence integrity before and after analysis       |
| `--report-html`             | Generate an HTML report                                    |
| `--report-pdf`              | Generate a PDF report                                      |

## Example Case Workflow

1. Create a forensic case report:

```bash
python -m pyforensickit.cli.main /var/log --output logs.json --case-id CASE-LOGS-01 --investigator "Jane Smith"
```

2. Verify evidence integrity and export full reports:

```bash
python -m pyforensickit.cli.main /home/user/evidence \
    --output case.json \
    --report-html case.html \
    --report-pdf case.pdf \
    --verify-integrity \
    --case-id CASE-2026-02 \
    --investigator "John Doe" \
    --description "Home directory analysis"
```

3. Export timeline for additional analysis:

```bash
python -m pyforensickit.cli.main /home/user/evidence --timeline-csv timeline.csv
```

## Forensic Considerations

- **Read-only analysis:** No evidence modification occurs.
- **Hashing:** Computes MD5, SHA1, and SHA256 directly from disk.
- **Integrity verification:** Evidence hashes are verified before and after analysis.
- **Offline workflow:** Designed to work without network connectivity.
- **Research and education:** Intended as a learning and investigative tool, not a replacement for enterprise forensic suites.

## Development & Contribution

- Modular design allows adding new forensic modules.
- Use `pytest` for running tests:

```bash
pytest -v --cov=src/pyforensickit
```

- Ensure all tests pass before submitting pull requests.

## Roadmap

- Timeline reconstruction improvements
- Deleted file recovery and analysis
- Email and browser artifact analysis
- Web-based reporting interface
- Integration with third-party forensic tools

## License

PyForensicKit is licensed under the [MIT License](LICENSE).

## References

- [Python `hashlib`](https://docs.python.org/3/library/hashlib.html)
- [Python `magic`](https://github.com/ahupp/python-magic)
- [Rich library for CLI visualization](https://rich.readthedocs.io/)
