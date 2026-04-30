from app.tools.k8s import restart_pod, rollback_deployment

def execute(decision: dict):
    action = decision["action"]
    target = decision["target"]

    if action == "restart_pod":
        restart_pod(target)

    elif action == "rollback_deployment":
        rollback_deployment(target)