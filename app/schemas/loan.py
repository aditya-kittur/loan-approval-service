from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class LoanRequest(BaseModel):
    model_config = ConfigDict(frozen=True)

    applicant_id: str = Field(..., min_length=1, description="Applicant UUID — cannot be blank")
    requested_amount: Decimal = Field(
        ...,
        gt=Decimal("9999"),
        lt=Decimal("5000001"),
        description="Loan amount must be between Rs.10,000 and Rs.50,00,000",
    )
    credit_score: int = Field(..., ge=300, le=900)
    annual_income: Decimal
    employment_status: Literal["SALARIED", "SELF_EMPLOYED", "UNEMPLOYED", "RETIRED"]


class LoanDecision(BaseModel):
    model_config = ConfigDict(frozen=True)

    applicant_id: str = Field(..., min_length=1, description="Applicant UUID — cannot be blank")
    status: Literal["APPROVED", "REJECTED"]
    interest_rate: Decimal | None
    reason: str = Field(..., min_length=2, max_length=500)