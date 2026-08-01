export interface LoanRequest {
  applicantId: string;
  requestedAmount: number;
  creditScore: number;
  annualIncome: number;
  employmentStatus: 'SALARIED' | 'SELF_EMPLOYED' | 'UNEMPLOYED' | 'RETIRED';
}

export interface LoanDecision {
  applicationId: number | null;
  status: 'APPROVED' | 'REJECTED';
  interestRate: number | null;
  message: string;
}
