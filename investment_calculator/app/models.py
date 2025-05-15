from pydantic import BaseModel

class InvestmentInput(BaseModel):
    principal: float
    rate: float
    time: int

class InvestmentOutput(BaseModel):
    total: float
