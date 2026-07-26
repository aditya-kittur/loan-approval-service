from fastapi import FastAPI
from app.routers.loans import router as loans_router
from app.routers.status import router as status_router

app = FastAPI(title="Loan Approval Service", version="1.0.0")
app.include_router(loans_router)
app.include_router(status_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
