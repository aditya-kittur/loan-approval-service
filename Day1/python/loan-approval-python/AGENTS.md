# AGENTS.md — loan-approval-python

## Service Overview
FastAPI REST service for retail banking loan approvals.
Evaluates loan eligibility using credit score, annual income, and employment status.
Returns a structured LoanDecision with status, interest rate, and reason.
Consumed by the mobile banking app and the branch portal.
Python 3.12. FastAPI 0.110+. Pydantic v2.

## Build and Run Commands
```bash
source .venv/bin/activate           # activate virtualenv first
pytest -v                            # run all tests
pytest tests/services/ -v            # run service tests only
uvicorn app.main:app --reload        # start development server (port 8000)
app/
  main.py              — FastAPI app creation and router registration
  routers/loans.py     — HTTP route handlers only, no business logic
  services/            — all business logic, class-based services
  schemas/loan.py      — Pydantic v2 request/response models
  models/              — SQLAlchemy ORM models (future use)
  middleware/          — ASGI middleware (future use)
tests/
  services/            — unit tests for service classes
  routers/             — integration tests using FastAPI TestClient
  Architecture Rules

Routers: HTTP layer only. Call service methods, return responses. Zero business logic.

Services: All business logic lives in class-based services. Stateless methods.

Schemas: Pydantic v2 models. Use model_config = ConfigDict(frozen=True) for immutability.

NEVER put business logic in route handlers.

NEVER use bare module-level functions for business logic — use class methods.

Coding Standards

Logging: Python logging module only. NEVER print(). Logger declaration: logger = logging.getLogger(__name__) at module level. Log calls: use %s lazy formatting — NEVER f-strings in log calls. Example: logger.info("Evaluating loan for: %s", request.applicant_id)

Type annotations: required on ALL function parameters and return types.

Decimal: ALWAYS use string constructor — Decimal("7.5") not Decimal(7.5).

Return empty list [] from functions that return collections when no data — NEVER return None.

Use | None union syntax (Python 3.10+) not Optional[X] from typing.

Docstrings: Google-style docstrings on all public methods and classes.
Test Standards

pytest only. NEVER unittest.TestCase.

Test file naming: test_{module_name}.py

Test function naming: test_{method}_given_{condition}_{expected_result}

Use Decimal("X") in test assertions — never float literals.

One assert per test function where possible.

Domain Glossary

Applicant: individual applying for the loan, identified by applicant_id (UUID string)

Credit Score: integer 300–900 on CIBIL scale. Below 600 is high risk.

Employment Status: one of SALARIED | SELF_EMPLOYED | UNEMPLOYED | RETIRED

Interest Rate: expressed as a percentage Decimal. 7.5 means 7.5% per annum.

What Agents Must Always Do
Run pytest -v after any code change

Add a Google-style docstring to every new public method

Use type annotations on all new functions

Place new service classes in app/services/

Place new route handlers in app/routers/