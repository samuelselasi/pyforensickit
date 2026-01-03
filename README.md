# PyForensicKit

> **PyForensicKit** is a Linux-based digital forensics command-line
toolkit designed to assist investigators in analyzing digital
evidence while preserving forensic integrity.

## Features

- Cryptographic hashing (MD5, SHA1, SHA256)
- File metadata extraction
- Read-only evidence analysis
- JSON, HTML, and PDF report generation
- Modular and extensible architecture
- File system timeline reconstruction
- CSV and JSON timeline export
- Evidence integrity verification

## Installation

```bash
git clone https://github.com/samuelselasi/pyforensickit.git
cd pyforensickit
pip install -r requirements.txt
```

## Usage

Basic JSON report:

```bash
python -m pyforensickit.cli.main /path/to/evidence --output report.json
```

Export timeline as CSV:

```bash
python -m pyforensickit.cli.main /path/to/evidence --timeline-csv timeline.csv
```

Generate HTML and PDF reports with integrity verification:

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

### Forensic Considerations

- No evidence modification
- Hashes computed directly from disk
- Integrity of evidence verified before and after analysis
- Designed for offline analysis
- Intended for educational and research purposes

### Roadmap

- Timeline reconstruction improvements
- Deleted file detection
- Email and browser artifact analysis
- Web interface for visual reporting

