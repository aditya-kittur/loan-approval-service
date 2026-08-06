using LoanApproval.Models;

namespace LoanApproval.Services;

// TODO: this service has problems for Lab 1 to fix

public class LoanApprovalService
{
    public LoanDecision Evaluate(LoanRequest request)
    {
        Console.WriteLine($"Evaluating loan for: {request.ApplicantId}"); // bad practice

        if (request.CreditScore <= 0)
            return new LoanDecision(request.ApplicantId, "REJECTED", null, "Credit score missing");

        if (request.CreditScore >= 750)
            return new LoanDecision(request.ApplicantId, "APPROVED", 7.5m, "Excellent profile");

        if (request.CreditScore >= 600)
            return new LoanDecision(request.ApplicantId, "APPROVED", 12.0m, "Standard profile");

        return new LoanDecision(request.ApplicantId, "REJECTED", null, "Credit score too low");
    }
}
