namespace LoanApproval.Models;

public record LoanDecision(
    string ApplicantId,
    string Status,
    decimal? InterestRate,
    string Reason
);