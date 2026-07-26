from decimal import Decimal
from pydantic import BaseModel


class ApplicantProfileRequest(BaseModel):
    applicant_id: str
    full_name: str
    pan_number: str         # Indian PAN: 5 letters + 4 digits + 1 letter (AAAAA9999A)
    email_address: str
    mobile_number: str       # 10-digit Indian mobile starting with 6-9
    net_worth: Decimal | None = None
    dependents: int | None = None