from fastapi import APIRouter
from app.schemas.loan import LoanDecision, LoanRequest
from app.services.loan_service import evaluate_loan

router = APIRouter(prefix="/api/loans", tags=["loans"])


@router.post("/evaluate", response_model=LoanDecision)
def evaluate(request: LoanRequest) -> LoanDecision:
    return evaluate_loan(request)