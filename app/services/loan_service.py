# TODO: this service has problems for Lab 1 to fix

from app.schemas.loan import LoanDecision, LoanRequest
from decimal import Decimal


def evaluate_loan(request: LoanRequest) -> LoanDecision:
    print(f"Evaluating loan for: {request.applicant_id}")  # bad practice

    if request.credit_score >= 750:
        return LoanDecision(
            applicant_id=request.applicant_id,
            status="APPROVED",
            interest_rate=Decimal("7.5"),
            reason="Excellent credit profile",
        )
    elif request.credit_score >= 600:
        return LoanDecision(
            applicant_id=request.applicant_id,
            status="APPROVED",
            interest_rate=Decimal("12.0"),
            reason="Standard credit profile",
        )
    else:
        return LoanDecision(
            applicant_id=request.applicant_id,
            status="REJECTED",
            interest_rate=None,
            reason="Credit score below minimum threshold",
        )