# Greenfield AgroWorks - Smart Irrigation Agent

## 1. The Problem


## 2. Agent Architectures
This repo contains 4 distinct architectures solving the exact same problem:
1. `reactive/`: Hard-coded if/then rules.
2. `unconstrained_react/`: A free-form LLM ReAct loop.
3. `routing/`: Single-call LLM classification followed by deterministic code.
4. `constrained_react/`: ReAct loop with Pydantic schema validation, allowed tools, and MAX_STEPS.

## 3. Comparison Table
| Agent Architecture | API Calls per Request | Approx. Cost / Tokens | Latency | Tricky Input Failure |
| :--- | :--- | :--- | :--- | :--- |
| **Reactive** | 0 | $0 | < 1 ms | Wasted water/flooded crops right before rain. |
| **Unconstrained** | ... | ... | ... | ... |
| **Routing** | ... | ... | ... | ... |
| **Constrained ReAct** | ... | ... | ... | ... |