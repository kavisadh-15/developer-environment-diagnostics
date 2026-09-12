# Developer Environment Diagnostics Tool
## Overview

Developer Environment Diagnostics Tool is a Python command-line tool that checks a developer machine and generates a health report.

It checks Python version, available disk space, important environment variables, and configured developer tools.

The tool provides both human-readable and JSON reports.
## Installation

Clone the repository and create a virtual environment.

```bash
python -m venv .venv
## Usage

Run the diagnostics tool:

```cmd
diagnostics
## Testing

Run the test suite with:

```cmd
python -m pytest
## Features

- Checks the installed Python version
- Checks available disk space
- Checks important environment variables
- Detects configured developer tools
- Generates human-readable reports
- Generates structured JSON reports
- Provides a command-line interface
- Includes automated unit tests
## Project Structure

```text
developer-environment-diagnostics/
├── src/
│   └── diagnostics/
│       ├── __init__.py
│       ├── checks.py
│       ├── report.py
│       └── cli.py
├── tests/
│   └── test_diagnostics.py
├── reports/
├── pyproject.toml
└── README.md