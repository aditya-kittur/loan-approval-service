from pydantic import BaseModel
from decimal import Decimal
from typing import Literal


class LoanRequest(BaseModel):
    applicant_id: str
    requested_amount: Decimal
    credit_score: int
    annual_income: Decimal
    employment_status: Literal["SALARIED", "SELF_EMPLOYED", "UNEMPLOYED", "RETIRED"]


class LoanDecision(BaseModel):
    applicant_id: str
    status: Literal["APPROVED", "REJECTED"]
    interest_rate: Decimal | None
    reason: str