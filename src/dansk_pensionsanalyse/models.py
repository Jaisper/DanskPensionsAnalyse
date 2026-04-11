from pydantic import BaseModel, Field
from typing import Literal


class InsuranceCoverage(BaseModel):
    name: str
    description: str | None = None


class PensionPlan(BaseModel):
    provider: str = Field(..., description="Navn på pensionsselskab eller bank")
    plan_type: Literal["ratepension", "livrente", "aldersopsparing", "ukendt"]
    balance_dkk: float | None = None
    monthly_contribution_dkk: float | None = None
    insurance_coverages: list[InsuranceCoverage] = Field(default_factory=list)


class SanitizedPayload(BaseModel):
    original_text_present: bool = False
    sanitized_text: str
    redactions: list[str] = Field(default_factory=list)
