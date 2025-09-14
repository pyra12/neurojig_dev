# NeuroJig

Skeleton of a Python application for ergonomic harness layout design.

## Modules
- **app** – entry points and dependency setup
- **core** – domain model, constraints, routing, lanes, optimization
- **ui** – PySide6 interface
- **data** – assets registry and persistence
- **services** – higher-level operations
- **tests** – test suite
- **docs** – documentation

## Getting Started
1. Install: `pip install -e .[dev]`
2. Set up pre-commit: `pre-commit install`
3. Run tests: `pytest`

## Running the App
After installation you can launch the graphical interface with:

```
python -m NeuroJig.app
```
