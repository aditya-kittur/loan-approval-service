import { z } from 'zod';

export interface LoanRequest {
  applicantId: string;
  requestedAmount: number;
  creditScore: number;
  annualIncome: number;
  employmentStatus: 'SALARIED' | 'SELF_EMPLOYED' | 'UNEMPLOYED' | 'RETIRED';
}

export interface LoanDecision {
  applicantId: string;
  status: 'APPROVED' | 'REJECTED';
  interestRate: number | null;
  reason: string;
}

export const LoanRequestSchema = z.object({
  applicantId: z.string().min(1, 'Applicant ID is required'),
  requestedAmount: z.number().min(10000).max(5000000),
  creditScore: z.number().int().min(300).max(900),
  annualIncome: z.number().min(0),
  employmentStatus: z.enum(['SALARIED', 'SELF_EMPLOYED', 'UNEMPLOYED', 'RETIRED']),
});

export type ValidatedLoanRequest = z.infer<typeof LoanRequestSchema>;

export const LoanDecisionSchema = z.object({
  applicantId: z.string().min(1, 'Applicant ID is required'),
  status: z.enum(['APPROVED', 'REJECTED']),
  interestRate: z.number().nullable(),
  reason: z.string().min(1),
});

export type ValidatedLoanDecision = z.infer<typeof LoanDecisionSchema>;
