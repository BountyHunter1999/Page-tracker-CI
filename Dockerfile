FROM python:3.11.2-slim-bullseye

RUN apt-get update && apt-get upgrade --yes

RUN useradd --create-home simpleflask
USER simpleflask
WORKDIR /home/simpleflask

ENV VIRTUALENV=/home/simpleflask/venv
RUN python3 -m venv ${VIRTUALENV}
ENV PATH="${VIRTUALENV}/bin:$PATH"

COPY --chown=simpleflask pyproject.toml constraints.txt ./
RUN python -m pip install --upgrade pip setuptools && \
    python -m pip install --no-cache-dir -c constraints.txt ".[dev]"

COPY --chown=simpleflask src/ src/
COPY --chown=simpleflask test/ test/

RUN python -m pip install . -c constraints.txt && \
    python -m pytest test/unit/ && \
    python -m flake8 src/ && \
    python -m isort src/ --check && \
    python -m black src/ --check --quiet && \
    python 0m pylint src/ --disable=C0114,C0116,R1705 && \
    python -m bandit -r src/ --quiet

CMD ["flake8", "--app", "page_tracker.app", "run", \
    "--host", "0.0.0.0", "--port", "5000"]