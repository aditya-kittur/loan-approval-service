import { useState, useEffect } from 'react';
import type { HealthStatus } from '../types/health.types';

export function useHealthStatus() {
  const [data, setData] = useState<HealthStatus | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    const fetchHealthStatus = async () => {
      try {
        setLoading(true);
        setError(null);

        const response = await fetch('http://localhost:3001/api/health', {
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`Failed to fetch health status: ${response.status} ${response.statusText}`);
        }

        const result = (await response.json()) as HealthStatus;
        setData(result);
      } catch (err) {
        if (err instanceof DOMException && err.name === 'AbortError') {
          return;
        }
        setError(err instanceof Error ? err.message : 'An error occurred');
      } finally {
        setLoading(false);
      }
    };

    fetchHealthStatus();

    return () => {
      controller.abort();
    };
  }, []);

  return { data, loading, error };
}
