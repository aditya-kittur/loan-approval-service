from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class LoanAmendmentRequest(BaseModel):
    model_config = ConfigDict(frozen=True)

    application_id: str = Field(
        ..., min_length=1, description="Application UUID — cannot be blank"
    )
    new_requested_amount: Decimal = Field(
        ...,
        gt=Decimal("9999"),
        lt=Decimal("5000001"),
        description="Loan amount must be between Rs.10,000 and Rs.50,00,000",
    )
    reason: str = Field(..., min_length=2, max_length=500)
    