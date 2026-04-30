def require_approval(decision: dict) -> bool:
    if decision["action"] in ["rollback_deployment"]:
        user_input = input(f"Approve action {decision}? (y/n): ")
        return user_input.lower() == "y"
    return True