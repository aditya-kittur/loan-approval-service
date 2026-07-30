import logging
from decimal import Decimal

from app.schemas.loan import LoanDecision, LoanRequest

logger = logging.getLogger(__name__)


class LoanService:
    """Service for evaluating loan applications and retrieving stored decisions."""

    def __init__(self) -> None:
        self._decisions: list[LoanDecision] = []

    def evaluate(self, request: LoanRequest) -> LoanDecision:
        """Evaluate a loan request and store the resulting decision."""
        logger.info("Evaluating loan for: %s", request.applicant_id)

        if request.credit_score >= 750:
            decision = LoanDecision(
                applicant_id=request.applicant_id,
                status="APPROVED",
                interest_rate=Decimal("7.5"),
                reason="Excellent credit profile",
            )
        elif request.credit_score >= 600:
            decision = LoanDecision(
                applicant_id=request.applicant_id,
                status="APPROVED",
                interest_rate=Decimal("12.0"),
                reason="Standard credit profile",
            )
        else:
            decision = LoanDecision(
                applicant_id=request.applicant_id,
                status="REJECTED",
                interest_rate=None,
                reason="Credit score below minimum threshold",
            )

        self._decisions.append(decision)
        return decision

    def get_decisions(self, applicant_id: str) -> list[LoanDecision]:
        """Return decisions for an applicant sorted by interest rate ascending."""
        applicant_decisions = [
            decision for decision in self._decisions if decision.applicant_id == applicant_id
        ]
        return sorted(applicant_decisions, key=self._sort_key)

    @staticmethod
    def _sort_key(decision: LoanDecision) -> tuple[bool, Decimal]:
        if decision.interest_rate is None:
            return (True, Decimal("Infinity"))
        return (False, decision.interest_rate)


def evaluate_loan(request: LoanRequest) -> LoanDecision:
    """Evaluate a loan request using the service layer."""
    return LoanService().evaluate(request)