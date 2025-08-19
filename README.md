# Playwright Python Example

This template demonstrates how to write an end-to-end test using [Playwright](https://playwright.dev/python) and `pytest` for UI regression testing.

The included test opens the QBench login page at `https://srqaengineer-sf-uat.qbench.net/` and checks the page against a stored screenshot.

## Setup

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
