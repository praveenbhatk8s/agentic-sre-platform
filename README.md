# Agentic SRE: Incident Triage & Remediation System

## Overview
This project demonstrates an agentic AI system designed to automate incident triage and remediation in cloud-native environments.

The system listens to alerts, gathers context from logs and metrics, and proposes or executes remediation actions with built-in safety guardrails.

## Key Features
- Agent-based incident triage workflow
- Integration with Kubernetes and observability signals
- Tool-based architecture (logs, metrics, k8s actions)
- Safe execution with approval guardrails
- Extensible design for real-world platform engineering use cases

## Architecture
See ARCHITECTURE.md

## How It Works
1. Receive alert (via API)
2. Gather logs and metrics
3. Analyze using LLM logic
4. Suggest remediation
5. Require approval for critical actions
6. Execute action

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload