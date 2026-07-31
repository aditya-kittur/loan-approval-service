import { z } from 'zod';

export interface CreditBureauRequest {
  panNumber: string;
  bureauName: string;
  consentToken: string;
}

export const CreditBureauRequestSchema = z.object({
  panNumber: z.string().regex(/^[A-Z]{5}[0-9]{4}[A-Z]{1}$/, 'Invalid PAN format'),
  bureauName: z.enum(['CIBIL', 'EXPERIAN', 'CRIF']),
  consentToken: z.string().min(1, 'Consent token is mandatory'),
});

export type ValidatedCreditBureauRequest = z.infer<typeof CreditBureauRequestSchema>;