---

# 🧱 ARCHITECTURE.md

```markdown
# Architecture

## High-Level Flow

Alert → Agent → Tools → LLM → Decision → Guardrails → Execution

## Components

### 1. Alert Ingestion
Receives alerts via HTTP endpoint (simulating Alertmanager / CloudWatch)

### 2. Agent Orchestrator
Coordinates workflow:
- Context gathering
- LLM reasoning
- Decision handling

### 3. Tools Layer
- Logs tool (Kubernetes logs)
- Metrics tool (Prometheus or mock)
- Kubernetes tool (actions)

### 4. LLM Layer
Analyzes context and outputs structured decisions

### 5. Guardrails
Prevents unsafe actions:
- Approval required for destructive operations

### 6. Executor
Applies changes to infrastructure

## Design Principles
- Safe by default
- Observable decisions
- Tool-based deterministic execution
- Extensible platform architecture