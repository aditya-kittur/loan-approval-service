import express from 'express';
import cors from 'cors';
import { evaluateLoan } from './loan/loan.service';
import { LoanRequest } from './loan/loan.types';
import { HealthStatus } from './types/health.types';

const app = express();
app.use(cors());
app.use(express.json());

app.post('/api/loans/evaluate', (req, res) => {
  const decision = evaluateLoan(req.body as LoanRequest);
  res.json(decision);
});

app.get('/api/health', (_req, res) => {
  const health: HealthStatus = {
    status: 'ok',
    service: 'loan-approval-service',
    uptime: Math.floor(process.uptime()),
  };
  res.json(health);
});

if (require.main === module) {
  app.listen(3001, () => console.log('Loan API running on port 3001'));
}

export { app };
