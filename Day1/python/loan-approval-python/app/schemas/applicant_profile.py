import re
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ApplicantProfileRequest(BaseModel):
    model_config = ConfigDict(frozen=True)

    applicant_id: str = Field(..., min_length=1, description="Applicant UUID — cannot be blank")
    full_name: str = Field(..., min_length=2, max_length=100)
    pan_number: str  # Indian PAN: 5 letters + 4 digits + 1 letter (AAAAA9999A)
    email_address: str
    mobile_number: str  # 10-digit Indian mobile starting with 6-9
    net_worth: Decimal | None = Field(default=None, ge=Decimal("0"))
    dependents: int | None = Field(default=None, ge=0)

    @field_validator("pan_number")
    @classmethod
    def validate_pan_number(cls, value: str) -> str:
        """Validate PAN format using the Indian PAN pattern."""
        if not re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", value):
            raise ValueError("Invalid PAN format. Expected: AAAAA9999A")
        return value

    @field_validator("email_address")
    @classmethod
    def validate_email_address(cls, value: str) -> str:
        """Validate email address format."""
        if "@" not in value or "." not in value.split("@", 1)[1]:
            raise ValueError("Invalid email address format")
        return value

    @field_validator("mobile_number")
    @classmethod
    def validate_mobile_number(cls, value: str) -> str:
        """Validate Indian mobile number format."""
        if not re.fullmatch(r"^[6-9]\d{9}$", value):
            raise ValueError("Invalid Indian mobile number — must be 10 digits starting with 6-9")
        return value