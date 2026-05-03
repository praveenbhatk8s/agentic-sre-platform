# Architecture

The platform is built around a small agent loop: ingest alert, gather context, reason over the situation, apply guardrails, and execute only approved actions.

```mermaid
flowchart TB
  subgraph Input["Inputs"]
    Alert["Alert payload"]
    K8sSignals["Kubernetes state"]
    MetricsSignals["Metrics"]
    LogSignals["Logs"]
  end

  subgraph Agent["Agent Runtime"]
    Orchestrator["Agent orchestrator"]
    Tools["Tools layer"]
    Decision["Decision layer"]
    Guardrails["Guardrails"]
    Executor["Executor"]
  end

  subgraph Actions["Actions"]
    Suggest["Suggest remediation"]
    Execute["Execute approved action"]
    Escalate["Ask for human approval"]
  end

  Alert --> Orchestrator
  Orchestrator --> Tools
  K8sSignals --> Tools
  MetricsSignals --> Tools
  LogSignals --> Tools
  Tools --> Decision
  Decision --> Guardrails
  Guardrails --> Suggest
  Guardrails --> Escalate
  Guardrails --> Executor
  Executor --> Execute
```

## Components

| Component | Responsibility |
| --- | --- |
| FastAPI entrypoint | Receives alert payloads through `/alert` |
| Agent orchestrator | Coordinates context gathering and decision flow |
| Logs tool | Fetches workload logs |
| Metrics tool | Fetches service health signals |
| Kubernetes tool | Provides cluster action hooks |
| Decision layer | Produces a structured remediation recommendation |
| Guardrails | Requires approval for risky actions |
| Executor | Performs approved remediation |

## Sequence

```mermaid
sequenceDiagram
  participant Alert as Alert Source
  participant API as FastAPI
  participant Agent as Agent
  participant Tools as Tools
  participant Decision as Decision Layer
  participant Guard as Guardrails
  participant Exec as Executor

  Alert->>API: POST /alert
  API->>Agent: run_agent(alert)
  Agent->>Tools: get metrics and logs
  Tools-->>Agent: context
  Agent->>Decision: analyze context
  Decision-->>Agent: proposed action
  Agent->>Guard: evaluate action risk
  Guard-->>Agent: allow or require approval
  Agent->>Exec: execute approved action
  Exec-->>Agent: execution result
  Agent-->>API: decision response
```

## Design Principles

- Safe by default
- Tool-based execution instead of arbitrary shell access
- Human approval for destructive operations
- Clear separation between reasoning and execution
- Extensible integrations for real observability systems
