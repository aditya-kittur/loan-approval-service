import { useState } from 'react';
import type { LoanDecision, LoanRequest } from '../types/loan.types';

// TODO: this hook has problems for Lab 1 to fix

export function useLoanApproval() {
  const [decision, setDecision] = useState<LoanDecision | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const evaluate = async (request: LoanRequest) => {
    try {
      setLoading(true);
      setError(null);
      const response = await fetch('http://localhost:3001/api/loans/evaluate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(request),
      });
      const data = await response.json();
      setDecision(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return { decision, loading, error, evaluate };
}
