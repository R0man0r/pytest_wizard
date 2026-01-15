# Pytest Wizard UI Tests

## Requirements
- Python 3.10+
- Google Chrome / Firefox
- pip

> Important: activate venv before running tests
## Setup virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## Upgrade pip (optional)
```bash
pip install --upgrade pip
```
## Install dependencies
```bash
pip install -r requirements.txt
```
## Run tests

### Run full wizard flow
```bash
pytest tests/test_wizard.py
```
### Run test for a specific page by name
```bash
pytest tests/test_separate_pages -k test_name
```
