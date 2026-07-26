from pydantic import BaseModel
from typing import Literal


class CreditBureauRequest(BaseModel):
    pan_number: str
    bureau_name: Literal["CIBIL", "EXPERIAN", "CRIF"]
    consent_token: str       # mandatory — legal requirement