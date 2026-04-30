import subprocess

def restart_pod(pod_name: str):
    print(f"[ACTION] Restarting pod {pod_name}")
    # subprocess.run(["kubectl", "delete", "pod", pod_name])

def rollback_deployment(deployment: str):
    print(f"[ACTION] Rolling back deployment {deployment}")
    # subprocess.run(["kubectl", "rollout", "undo", f"deployment/{deployment}"])