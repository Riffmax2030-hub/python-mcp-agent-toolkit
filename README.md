# 🔌 Python MCP Agent Toolkit

> **Modular Model Context Protocol (MCP) servers and tool-calling agent framework in Python** — demonstrates how LLMs interact safely with local tools, APIs, and file systems.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![MCP Protocol](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-orange)](https://modelcontextprotocol.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

---

## 📌 What it does

The **Model Context Protocol (MCP)** is the open standard enabling LLMs to execute secure tools, query data sources, and automate workflows. This repository provides:

- 🛠️ **Reusable Custom MCP Servers** — Exposes sandboxed tools for data transformation, math calculations, and filesystem auditing.
- 🤖 **Tool-Calling Agent Orchestrator** — Parses model tool-call intents, enforces input validation, dispatches execution, and formats feedback into conversation context.
- 🛡️ **Sandbox Security Guardrails** — Enforces path traversal prevention, timeout boundaries, and permission whitelists.
- ⚡ **Asynchronous Execution Loop** — High-performance non-blocking I/O using Python's `asyncio`.

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────────────┐
│                   LLM Reasoning Core                   │
│         Selects tool calls based on user request       │
└───────────────────────────┬────────────────────────────┘
                            │
               Model Context Protocol (MCP)
                            │
┌───────────────────────────▼────────────────────────────┐
│                  Agent Dispatcher / Loop               │
│   • Input Validation  • Path Traversal Guards          │
│   • Execution Logging • State Management               │
└───────────────────────────┬────────────────────────────┘
                            │
┌───────────────────────────▼────────────────────────────┐
│                   Modular MCP Servers                  │
│   • DataAnalysisServer   • FileAuditorServer           │
└────────────────────────────────────────────────────────┘
```

---

## 🛠️ Stack

| Component | Technology | Description |
|---|---|---|
| **Core Language** | Python 3.10+ | Async agent dispatcher and tool implementations |
| **Protocol** | Model Context Protocol (MCP) | Open standard for LLM tool integration |
| **Validation** | Pydantic | Typed schemas for tool arguments and results |
| **Concurrency** | Asyncio | Concurrent tool invocation and non-blocking I/O |

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/Riffmax2030-hub/python-mcp-agent-toolkit.git
cd python-mcp-agent-toolkit
pip install -r requirements.txt
```

### 2. Run the Agent Tool-Use Demo

```bash
python run_agent.py
```

### 3. Run Test Suite

```bash
python -m unittest discover tests
```

---

## 📁 Project Structure

```
python-mcp-agent-toolkit/
├── servers/
│   ├── __init__.py
│   ├── base.py               # Abstract Base MCP Server
│   └── data_tools_server.py  # Data transformation & math tools
├── toolkit/
│   ├── __init__.py
│   ├── agent.py              # Autonomous tool-calling agent loop
│   └── security.py           # Path validation & parameter guards
├── tests/
│   └── test_agent.py         # Agent execution unit tests
├── run_agent.py              # CLI demonstration script
├── requirements.txt
└── README.md
```

---

## 🧠 Tool Schema Definition Example

```python
{
  "name": "calculate_statistics",
  "description": "Calculates mean, median, and variance for a numeric sequence.",
  "parameters": {
    "type": "object",
    "properties": {
      "numbers": {
        "type": "array",
        "items": {"type": "number"}
      }
    },
    "required": ["numbers"]
  }
}
```

---

## 📄 License

MIT © [Sherif Akanmu](https://github.com/Riffmax2030-hub)
