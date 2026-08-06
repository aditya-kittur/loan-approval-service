namespace LoanApproval.Models;

public class LoanRequest
{
    public string ApplicantId { get; set; } = string.Empty;
    public decimal RequestedAmount { get; set; }
    public int CreditScore { get; set; }
    public decimal AnnualIncome { get; set; }
    public string EmploymentStatus { get; set; } = string.Empty;
}