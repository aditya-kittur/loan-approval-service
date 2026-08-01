import { useState } from 'react'
import { useLoanApproval } from './hooks/useLoanApproval'
import type { LoanRequest } from './types/loan.types'

const initialForm: LoanRequest = {
  applicantId: '',
  requestedAmount: 0,
  creditScore: 0,
  annualIncome: 0,
  employmentStatus: 'SALARIED',
}

function App() {
  const [form, setForm] = useState<LoanRequest>(initialForm)
  const { decision, loading, error, evaluate } = useLoanApproval()

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target
    setForm(prev => ({
      ...prev,
      [name]: name === 'requestedAmount' || name === 'creditScore' || name === 'annualIncome'
        ? Number(value)
        : value,
    }))
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    evaluate(form)
  }

  return (
    <div style={{ maxWidth: 480, margin: '48px auto', padding: '0 16px' }}>
      <h1>Loan Approval Service</h1>

      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        <label>
          Applicant ID
          <input name="applicantId" value={form.applicantId} onChange={handleChange} required style={inputStyle} />
        </label>
        <label>
          Requested Amount ($)
          <input name="requestedAmount" type="number" min={1} value={form.requestedAmount} onChange={handleChange} required style={inputStyle} />
        </label>
        <label>
          Credit Score
          <input name="creditScore" type="number" min={300} max={850} value={form.creditScore} onChange={handleChange} required style={inputStyle} />
        </label>
        <label>
          Annual Income ($)
          <input name="annualIncome" type="number" min={0} value={form.annualIncome} onChange={handleChange} required style={inputStyle} />
        </label>
        <label>
          Employment Status
          <select name="employmentStatus" value={form.employmentStatus} onChange={handleChange} style={inputStyle}>
            <option value="SALARIED">Salaried</option>
            <option value="SELF_EMPLOYED">Self-Employed</option>
            <option value="UNEMPLOYED">Unemployed</option>
            <option value="RETIRED">Retired</option>
          </select>
        </label>
        <button type="submit" disabled={loading} style={buttonStyle}>
          {loading ? 'Evaluating…' : 'Apply for Loan'}
        </button>
      </form>

      {error && (
        <div style={{ ...alertStyle, background: '#fdecea', borderColor: '#f44336', color: '#b71c1c' }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {decision && decision.status === 'APPROVED' && (
        <div style={{ ...alertStyle, background: '#e8f5e9', borderColor: '#4caf50', color: '#1b5e20' }}>
          <strong>✅ Loan Approved!</strong>
          <p style={{ margin: '8px 0 0' }}>{decision.message}</p>
          {decision.interestRate !== null && (
            <p style={{ margin: '4px 0 0' }}>Interest Rate: <strong>{decision.interestRate}%</strong></p>
          )}
        </div>
      )}

      {decision && decision.status === 'REJECTED' && (
        <div style={{ ...alertStyle, background: '#fff3e0', borderColor: '#ff9800', color: '#e65100' }}>
          <strong>❌ Loan Rejected</strong>
          <p style={{ margin: '8px 0 0' }}>{decision.message}</p>
        </div>
      )}
    </div>
  )
}

const inputStyle: React.CSSProperties = {
  display: 'block',
  width: '100%',
  marginTop: 4,
  padding: '8px 10px',
  fontSize: 14,
  boxSizing: 'border-box',
}

const buttonStyle: React.CSSProperties = {
  padding: '10px 20px',
  fontSize: 16,
  cursor: 'pointer',
}

const alertStyle: React.CSSProperties = {
  marginTop: 24,
  padding: '16px',
  border: '1px solid',
  borderRadius: 4,
}

export default App
