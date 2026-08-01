import { z } from 'zod';

export interface ApplicantProfileRequest {
  applicantId: string;
  fullName: string;
  panNumber: string;
  emailAddress: string;
  mobileNumber: string;
  netWorth?: number;
  dependents?: number;
}

export const ApplicantProfileRequestSchema = z.object({
  applicantId: z.string().min(1, 'Applicant ID is required'),
  fullName: z.string().min(2).max(100),
  panNumber: z.string().regex(/^[A-Z]{5}[0-9]{4}[A-Z]{1}$/, 'Invalid PAN format'),
  emailAddress: z.string().email('Invalid email address'),
  mobileNumber: z.string().regex(/^[6-9]\d{9}$/, 'Invalid Indian mobile number'),
  netWorth: z.number().min(0).optional(),
  dependents: z.number().int().min(0).optional(),
});

export type ValidatedApplicantProfileRequest = z.infer<typeof ApplicantProfileRequestSchema>;