import litellm
from pypdf import PdfReader
from .models.output_schema import AuditResult


class Agent:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model

    def audit_document(self, file_path: str) -> AuditResult:
        # Load document content
        reader = PdfReader(file_path)
        content = ""
        for page in reader.pages:
            content += page.extract_text()

        # Simulate AI audit (placeholder)
        # In real, use litellm to call LLM for risk assessment
        # For now, mock based on content length
        risk_score = min(10, len(content) // 100)  # Simple mock
        high_risk_clause = "Potential data breach clause" if risk_score > 5 else "None"

        return AuditResult(
            document_id=file_path,
            risk_score=risk_score,
            high_risk_clause=high_risk_clause
        )
