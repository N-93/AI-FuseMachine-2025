from fastapi import FastAPI
from app.models import InvestmentInput, InvestmentOutput
from app.config import settings

app = FastAPI(title=settings.app_name)

@app.post("/calculate", response_model=InvestmentOutput)
def calculate_investment(data: InvestmentInput):
    total = data.principal * (1 + data.rate) ** data.time
    return InvestmentOutput(total=round(total, 2))

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.app_name}"}
