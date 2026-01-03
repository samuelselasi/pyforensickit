# PyForensicKit

> **PyForensicKit** is a Linux-based digital forensics command-line 
toolkit designed to assist investigators in analyzing digital 
evidence while preserving forensic integrity.

## Features

- Cryptographic hashing (MD5, SHA1, SHA256)
- File metadata extraction
- Read-only evidence analysis
- JSON report generation
- Modular and extensible architecture

## Installation

```

git clone https://github.com/yourusername/pyforensickit.git
cd pyforensickit
pip install -r requirements.txt

```

## Usage

```

python -m pyforensickit.cli.main /path/to/evidence --output report.json

```

### Forensic Considerations

- No evidence modification
- Hashes computed directly from disk
- Designed for offline analysis
- Intended for educational and research purposes

### Roadmap

- Timeline reconstruction
- Deleted file detection
- Email and browser artifact analysis
- Web interface


