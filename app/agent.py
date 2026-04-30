from app.tools.logs import get_logs
from app.tools.metrics import get_metrics
from app.llm import call_llm
from app.guardrails import require_approval
from app.executor import execute

def run_agent(alert: dict):
    context = {
        "alert": alert,
        "metrics": get_metrics(alert["service"]),
        "logs": get_logs("example-pod")
    }

    decision = call_llm(context)

    if require_approval(decision):
        execute(decision)
        decision["executed"] = True
    else:
        decision["executed"] = False

    return decision