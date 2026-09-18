# Hermes Test Project

Test repository for Hermes Agent GitHub integration.

## Purpose
Validate that Hermes can:
- Authenticate with GitHub via PAT
- Create/clone repositories
- Read/write files
- Commit and push changes
- Manage issues, PRs, workflows

## Structure
```
.
├── README.md
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── pyproject.toml
└── LICENSE
```

## Quick Start
```bash
pip install -e .
pytest
```
