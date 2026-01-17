# nw-psychiatry-hub

## Prerequisites

- Python 3.11+

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and adjust values as needed.

## Running the app

From the repo root, run either of the following:

```
python -m app.main
```

or

```
python app/main.py
```

## Architecture overview

The application is organized into a small set of top-level packages under
`northwest_psych_hub/`:

- `app/`: application entry point and startup wiring.
- `config/`: configuration utilities and environment handling.
- `services/`: domain/service logic.
- `ui/`: presentation/UI layer.

Add new modules in the package that matches their responsibility. For example,
business logic should live in `services/`, while UI components should be placed
in `ui/`. If you add a new domain area, create a subpackage within the relevant
top-level package.

## Project structure

```
northwest_psych_hub/
├── app/
│   ├── __init__.py
│   └── main.py
├── config/
│   └── __init__.py
├── services/
│   └── __init__.py
└── ui/
    └── __init__.py
```

## Environment configuration

Copy `.env.example` to `.env` and adjust values as needed. The application reads these
settings at startup using `python-dotenv` and `os.getenv`. Local config files (such as
`.env`) are intended for developer-specific overrides and should not be committed.

Example:

```
APP_NAME=Northwest Psychiatry Hub
LOG_LEVEL=INFO
```
