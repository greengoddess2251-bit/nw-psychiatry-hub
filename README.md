# nw-psychiatry-hub

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
settings at startup using `python-dotenv` and `os.getenv`.

Example:

```
APP_NAME=Northwest Psychiatry Hub
LOG_LEVEL=INFO
```
