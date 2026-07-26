import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class CreditBureauRequest(BaseModel):
    model_config = ConfigDict(frozen=True)

    pan_number: str
    bureau_name: Literal["CIBIL", "EXPERIAN", "CRIF"]
    consent_token: str = Field(
        ..., min_length=1, description="Consent token is mandatory for bureau queries"
    )  # mandatory — legal requirement

    @field_validator("pan_number")
    @classmethod
    def validate_pan_number(cls, value: str) -> str:
        """Validate PAN format using the Indian PAN pattern."""
        if not re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", value):
            raise ValueError("Invalid PAN format. Expected: AAAAA9999A")
        return value