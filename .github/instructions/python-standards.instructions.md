---
applyTo: "**/*.py"
---

# Python Coding Standards — loan-approval-python

## Python Version and Style
- Python 3.12. Use modern syntax: `X | None` not `Optional[X]`, `list[X]` not `List[X]`.
- Type annotations required on all function parameters and return types.
- Google-style docstrings on all public methods: Args, Returns, Raises sections.

## Framework
- FastAPI 0.110+. Pydantic v2. pytest.
- Route handlers use async def only when the handler calls an async dependency.
- For sync handlers (no database, no async I/O): use plain `def`.

## Logging
- `import logging` at top of every module that logs.
- `logger = logging.getLogger(__name__)` at module level — NOT inside functions.
- Use `%s` lazy string formatting in all log calls — NEVER f-strings in log calls.
- Log levels: DEBUG for tracing, INFO for business events, WARNING for recoverable issues, ERROR for failures.
- NEVER print(). NEVER logging.basicConfig() inside application code.

## Decimal and Numeric Precision
- Financial values always use `from decimal import Decimal`.
- ALWAYS use string constructor: `Decimal("7.5")` — NEVER `Decimal(7.5)`.
- NEVER use float for financial calculations.

## Collections and None Safety
- Functions returning collections return `[]` or `{}` on empty — NEVER return `None`.
- Use `X | None` for optional values. Always check before using.

## Class Design
- Business logic lives in class-based services — not module-level functions.
- Services are instantiated once at module level in the router — not inside route handlers.
- `__init__` takes only dependencies (for testability) — not request data.

## Tests
- pytest functions only. NEVER `unittest.TestCase`.
- Test naming: `test_{method}_given_{condition}_{expected_result}`.
- Use `Decimal("X")` in assertions — never float.
- Import from `app.*` using absolute imports.