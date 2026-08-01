import request from 'supertest';
import { app } from './index';

describe('GET /api/health', () => {
  test('GET /api/health returns 200 with status ok', async () => {
    const response = await request(app).get('/api/health');

    expect(response.status).toBe(200);
    expect(response.body.status).toBe('ok');
  });
});
