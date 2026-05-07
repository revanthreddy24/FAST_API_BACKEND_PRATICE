from pydantic import BaseModel
from typing import Literal


class PredictionRequest(BaseModel):
    text: str
    category: Literal[
        "healthcare_claims",
        "finance_fraud",
        "customer_support",
        "general"
    ]


class PredictionResponse(BaseModel):
    input_text: str
    category: str
    prediction: str
    confidence: float
    request_id: str


class HealthResponse(BaseModel):
    status: str
    app_name: str
    environment: str