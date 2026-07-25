from fastapi import FastAPI
from app.routers.loans import router as loans_router

app = FastAPI(title="Loan Approval Service", version="1.0.0")
app.include_router(loans_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}