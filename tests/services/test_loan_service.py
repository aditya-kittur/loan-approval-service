import pytest
from decimal import Decimal
from app.schemas.loan import LoanRequest
from app.services.loan_service import evaluate_loan


def make_request(credit_score: int) -> LoanRequest:
    return LoanRequest(
        applicant_id="TEST-001",
        requested_amount=Decimal("100000"),
        credit_score=credit_score,
        annual_income=Decimal("800000"),
        employment_status="SALARIED",
    )


def test_evaluate_loan_given_excellent_credit_returns_approved_at_seven_point_five():
    result = evaluate_loan(make_request(780))
    assert result.status == "APPROVED"
    assert result.interest_rate == Decimal("7.5")


def test_evaluate_loan_given_standard_credit_returns_approved_at_twelve():
    result = evaluate_loan(make_request(650))
    assert result.status == "APPROVED"
    assert result.interest_rate == Decimal("12.0")


def test_evaluate_loan_given_low_credit_returns_rejected():
    result = evaluate_loan(make_request(500))
    assert result.status == "REJECTED"
    assert result.interest_rate is None