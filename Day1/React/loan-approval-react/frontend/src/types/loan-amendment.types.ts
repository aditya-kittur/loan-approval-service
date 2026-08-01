import { z } from 'zod';

export interface LoanAmendmentRequest {
  applicationId: string;
  newRequestedAmount: number;
  reason: string;
}

export const LoanAmendmentRequestSchema = z.object({
  applicationId: z.string().uuid('Must be a valid UUID'),
  newRequestedAmount: z.number().min(10000).max(5000000),
  reason: z.string().min(1),
});

export type ValidatedLoanAmendmentRequest = z.infer<typeof LoanAmendmentRequestSchema>;