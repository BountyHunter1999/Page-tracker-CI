# Page-tracker-CI

![Program Architecture](./DOC_IMAGES/architecture.png)

# Dev

**Install dependencies for development purposes**

- `pip install --editable ".[dev]"` OR,
  - `pip install - ".[dev]"`

**Run tests**

- `python -m pytest -v test/unit/`
- `pytest -v test/e2e/ --flask-url http://127.0.0.1:5000 --redis-url redis://127.0.0.1:6379`

# Static Code Analysis

- `black src/ --check`: flag any formatting inconsistencies
- `isort src/ --check`: ensure our `import` statements stay organized according to [official recommendation](https://peps.python.org/pep-0008/#imports)
- `flake8 src/`: check for any other PEP 8 style violations
