import json

def call_llm(context: dict):
    # Mocked response for PoC (replace with OpenAI if needed)
    metrics = context["metrics"]

    if metrics["error_rate"] > 0.2:
        return {
            "issue": "High error rate likely due to bad deployment",
            "confidence": 0.85,
            "action": "rollback_deployment",
            "target": context["alert"]["service"],
            "reasoning": "Error spike detected after deployment"
        }

    return {
        "issue": "Unknown",
        "confidence": 0.5,
        "action": "no_action",
        "target": "",
        "reasoning": "Insufficient data"
    }