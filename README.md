# Page-tracker-CI

![Program Architecture](./DOC_IMAGES/architecture.png)

## Dev

**Install dependencies for development purposes**

- `pip install --editable ".[dev]"` OR,
  - `pip install - ".[dev]"`: run from within the web folder

**Run tests**

- `python -m pytest -v test/unit/`
- `pytest -v test/e2e/ --flask-url http://127.0.0.1:5000 --redis-url redis://127.0.0.1:6379`

## Static Code Analysis

- `black src/ --check`: flag any formatting inconsistencies
- `isort src/ --check`: ensure our `import` statements stay organized according to [official recommendation](https://peps.python.org/pep-0008/#imports)
- `flake8 src/`: check for any other PEP 8 style violations
- `pylint src/`: find code smells or ways to improve it

  - **E**: Errors
  - **W**: Warnings
  - **C**: Convention violations
  - **R**: Refactoring suggestions

  - To not stop even if `pylint` find an error `pylint src/ --exit-zero`
    - use `echo $?` to find the status code
  - to make it return a failed code if it doesn't reach certain threshold use `pylint src/ --fail-under 7.5`

> drop the `--check` flag to correct reported problems automatically

## Security Analysis

- `bandit -r src/`: make sure our application is secure before deploying the code to production

## Docker file name and tag

- `git rev-parse --short HEAD` to get the commit hash
- `docker build -t page-tracker:$(git rev-parse --short HEAD) .`

## Prod

- `pip install --editable "web/[dev]"`: run from root of the project
- `pip freeze --exclude-editable > web/constraints.txt`: this will help in creating wheels

### Test

- `pytest web/test/e2e/ --flask-url http://localhost --redis-url redis://localhost:6379`: local test