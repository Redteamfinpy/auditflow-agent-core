import typer
from pathlib import Path
from src.core.agent import Agent
from src.core.telemetry import send_trace_log

app = typer.Typer()


@app.command()
def audit_file(file_path: str = typer.Option(..., "--file-path", help="Path to the document to audit"),
               opt_in: bool = typer.Option(..., "--opt-in", help="Opt-in to telemetry")):
    """
    Audit a document file and output the result.
    """
    path = Path(file_path)
    if not path.exists():
        typer.echo(f"File {file_path} does not exist.")
        raise typer.Exit(1)

    # Instantiate Agent
    agent = Agent()

    # Audit
    result = agent.audit_document(file_path)

    # Send telemetry
    trace_data = {
        "document_id": result.document_id,
        "risk_score": result.risk_score,
        "error_type": "none"  # Placeholder
    }
    send_trace_log(trace_data, opt_in)

    # Print result
    typer.echo(f"Document ID: {result.document_id}")
    typer.echo(f"Risk Score: {result.risk_score}/10")
    typer.echo(f"High Risk Clause: {result.high_risk_clause}")


def main():
    app()


if __name__ == "__main__":
    main()
