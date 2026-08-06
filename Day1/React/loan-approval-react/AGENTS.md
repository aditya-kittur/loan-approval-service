# AGENTS.md — Loan Approval React/Express Service

## Overview
Full-stack loan evaluation service featuring an Express TypeScript backend and a React 18 TypeScript frontend scaffolded with Vite.

## Repository Layout
- `backend/`: Express REST API running on port 3001.
- `frontend/`: React 18 SPA running on port 5173.

## How to Build & Run
- Backend Dev: `cd backend && npm run dev`
- Frontend Dev: `cd frontend && npm run dev`
- Backend Build: `cd backend && npm run build`
- Frontend Build: `cd frontend && npm run build`

## Architecture Rules (Non-Negotiable)
1. **Backend Layer Separation:**
   - Routes (`index.ts`): Request routing only.
   - Services (`loan.service.ts`): Business logic, decision rules, and evaluation algorithms.
2. **Frontend State Management:**
   - Business logic and API calls MUST live inside custom hooks (`useLoanApproval.ts`), NOT directly inside UI components.
3. **Logging:**
   - Structured logging via `pino` only in the backend. Zero `console.log` statements in production backend code.

## Domain Glossary
- **`applicantId`**: Unique alphanumeric identifier for a loan applicant.
- **`creditScore`**: Integer between 300 and 850.
- **`requestedAmount`**: Total principal amount requested in local currency.
- **`employmentStatus`**: Enum (`'SALARIED' | 'SELF_EMPLOYED' | 'UNEMPLOYED' | 'RETIRED'`).

## What NOT to Touch
- `**/dist/` — Compiled output.
- `**/node_modules/` — Package dependencies.