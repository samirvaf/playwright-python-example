# Playwright Python Example

This repository shows how to exercise the QBench order workflow with
[Playwright](https://playwright.dev/python) and `pytest`.  The focus is on
functional UI tests.

> **Note**
> Playwright's Python bindings do not include native visual regression
> capabilities.  Integrating screenshot comparisons would require an external
> library, so this example omits that feature.

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

Environment variables `BASE_URL`, `USER_EMAIL`, and `USER_PASSWORD` may be
stored in a `.env` file or exported in the shell. The continuous integration
workflow expects these values to be provided through repository secrets.

## Running the tests

Execute the test suite:

```bash
pytest
```

Traces, screenshots, and videos are retained on failure by default.

## Project architecture

The code follows a simple Page Object Model:

- `tests/` contains pytest test cases.
- `ui/pages/` defines high‑level pages such as the login and order pages.
- `ui/sections/` holds smaller widgets used within pages.
- `ui/components/` contains reusable helpers like spinners and toasts.

## Extending the project

Future improvements could include:

- Adding more form fields with corresponding assertions.
- Introducing teardown logic that deletes created orders through API
  requests.
- Writing a new test that proves a Lab ID cannot be reused by creating an
  order through the API and attempting to reuse the same Lab ID via the UI.

## Highlights

- **Secrets Usage:**
  - Environment variables (`BASE_URL`, `USER_EMAIL`, `USER_PASSWORD`) are used for sensitive data and can be set in a `.env` file or exported in the shell. This keeps secrets out of the codebase and supports secure CI workflows.

- **Spinner Handling:**
  - UI tests include logic to detect and wait for spinners to disappear before interacting with page elements. This ensures reliable automation by synchronizing actions with the application's loading state.

- **Composition over Inheritance:**
  - Page objects are built using composition, not inheritance. Pages are assembled from smaller section and component objects, promoting code reuse and flexibility. This design avoids deep inheritance chains and makes the codebase easier to extend and maintain.

- **Test failures report:**
  - Test failures are uploaded to Github Actions artifacts including screenshots, logs and videos.

## AI Usage

Used a combination of ChatGPT, Codex and Github Copilot.
- ChatGPT for simple tasks and doubts about playwright API.
- Codex to build most of the boilerplate code.
- Github Copilot to speed up code writing.
