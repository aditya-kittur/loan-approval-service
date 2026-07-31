from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.loans import router as loans_router
from app.routers.status import router as status_router

app = FastAPI(title="Loan Approval Service", version="1.0.0")

# Allow the dashboard HTML (opened from file:// or any local dev server) to call the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

app.include_router(loans_router)
app.include_router(status_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
