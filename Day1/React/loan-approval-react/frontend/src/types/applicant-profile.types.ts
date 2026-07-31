export interface ApplicantProfileRequest {
  applicantId: string;
  fullName: string;
  panNumber: string;
  emailAddress: string;
  mobileNumber: string;
  netWorth?: number;
  dependents?: number;
}