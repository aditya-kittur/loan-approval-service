from pydantic import BaseModel
from decimal import Decimal


class LoanAmendmentRequest(BaseModel):
    application_id: str
    new_requested_amount: Decimal
    reason: str
    