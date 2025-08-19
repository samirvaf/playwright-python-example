# Playwright Python Example

This template demonstrates how to write an end-to-end test using [Playwright](https://playwright.dev/python) and `pytest` for UI regression testing.

The included test opens the QBench login page at `https://srqaengineer-sf-uat.qbench.net/` and checks the page against a stored screenshot.

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate
```

Install the dependencies and Playwright browsers:

```bash
pip install -r requirements.txt
playwright install
```

## Running the tests

On the first run, generate baseline screenshots:

```bash
pytest --update-snapshots
```

Subsequent runs will compare the current UI to the baseline:

```bash
pytest
```

## Run

Execute the test suite:

```bash
pytest
```

Traces, screenshots, and videos are retained on failure by default.
