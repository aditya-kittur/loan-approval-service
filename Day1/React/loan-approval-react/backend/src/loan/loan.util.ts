export function calculateMaxEligibleLoanAmount(income: number, creditScore: number): number {
  if (income <= 0 || creditScore <= 0) {
    return 0;
  }

  const baseAmount = income * 0.25;
  let scoreMultiplier = 0.5;

  if (creditScore >= 750) {
    scoreMultiplier = 1.0;
  } else if (creditScore >= 600) {
    scoreMultiplier = 0.8;
  }

  return Math.max(0, Math.floor(baseAmount * scoreMultiplier));
}
