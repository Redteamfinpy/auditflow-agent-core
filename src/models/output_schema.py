from pydantic import BaseModel


class AuditResult(BaseModel):
    document_id: str
    risk_score: int  # 1-10
    high_risk_clause: str
