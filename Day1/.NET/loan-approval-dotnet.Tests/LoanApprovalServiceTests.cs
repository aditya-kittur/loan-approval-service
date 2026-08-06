using LoanApproval.Models;
using LoanApproval.Services;

namespace LoanApproval.Tests;

public class LoanApprovalServiceTests
{
    private readonly LoanApprovalService _service = new();

    [Fact]
    public void Evaluate_GivenHighCreditScore_ReturnsApproved()
    {
        var request = new LoanRequest
        {
            ApplicantId = "APP001",
            CreditScore = 780,
            RequestedAmount = 100000,
            AnnualIncome = 800000,
            EmploymentStatus = "SALARIED"
        };

        var result = _service.Evaluate(request);

        Assert.Equal("APPROVED", result.Status);
        Assert.Equal(7.5m, result.InterestRate);
    }
}