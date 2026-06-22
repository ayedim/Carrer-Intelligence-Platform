# career-operations-intelligence-platform
AI-assisted career intelligence platform that automates opportunity discovery, extraction, evaluation, and resume routing using n8n, Gemini, Ollama, and Qwen. Designed as a human-in-the-loop decision-support system with strong emphasis on explainability, reliability, and workflow separation.
---

## Repository Structure

### `/Docs`

Project documentation and technical specifications.

Contents:

- System Specifications
- Technical Methodology
- Data Model Specification
- Prompt Engineering

These documents explain the architecture, design decisions, workflow logic, reliability controls, and implementation methodology used throughout the project.

---

### `/Pictures`

Architecture diagrams, workflow screenshots, and reporting examples.

Includes:

- n8n workflow screenshots
- Career Intelligence briefing examples
- Resume Routing workflow examples
- Input and output examples

---

### `/Examples`

Sanitized examples of the local resume-routing workflow.

Contents:

- `01_preprocess.py`
- `02_qwen_call.py`
- `03_report.py`
- Sample job inputs
- Sample routing outputs

These examples demonstrate workflow structure without exposing production data, credentials, or personal information.

---

## Architecture Overview

The platform consists of two independent workflows.

### Workflow A — Career Operations Intelligence

Responsible for:

- Opportunity ingestion
- Email processing
- Job extraction
- Deduplication
- Opportunity evaluation
- Strategic ranking
- Intelligence reporting

Primary technologies:

- Docker
- n8n
- Gmail API
- Gemini 2.5 Pro
- JavaScript
- Obsidian

---

### Workflow B — Resume Routing & Terminology Intelligence

Responsible for:

- Resume selection
- Terminology analysis
- Confidence scoring
- Application-support reporting

Primary technologies:

- Python
- Ollama
- Qwen 2.5 14B
- JSON
- Markdown

---

## Design Priorities

The project emphasizes:

- Explainability
- Reliability
- Traceability
- Workflow separation
- Human oversight

A significant portion of development focused on addressing common LLM failure modes, including:

- Hallucinations
- Schema inconsistency
- Unsupported assumptions
- Information loss
- Non-deterministic outputs

As a result, deterministic processing layers were introduced wherever possible, while AI systems were limited to tasks involving judgment, comparison, prioritization, and classification.

---

## Documentation Roadmap

Recommended reading order:

1. System Specifications
2. Technical Methodology
3. Data Model Specification
4. Prompt Engineering

---

## Technology Stack

### Workflow A

- Docker Desktop
- n8n
- Gmail API
- Gemini 2.5 Pro
- JavaScript
- Obsidian REST API

### Workflow B

- Python 3.13
- Ollama
- Qwen 2.5 14B
- JSON-based Resume Profiles
- Markdown Reporting

---

## Example Workflow

```text
External Job Sources
        ↓
Gmail Intake
        ↓
Opportunity Extraction
        ↓
Opportunity Evaluation
        ↓
Career Intelligence Brief
        ↓
Selected Opportunities
        ↓
Resume Routing
        ↓
Terminology Analysis
        ↓
Human Review
        ↓
Application Decision
```

---

## Project Goals

The platform was designed to improve:

- Opportunity prioritization
- Resume-role alignment
- Interview probability
- Career trajectory planning
- Application efficiency

While reducing:

- Decision fatigue
- Duplicate opportunities
- Low-fit applications
- Manual review overhead

---

## Status

Personal research and portfolio project.

The repository demonstrates practical applications of:

- Workflow automation
- AI-assisted decision support
- Prompt engineering
- Reliability engineering
- Human-in-the-loop system design
- Career intelligence workflows

The project is not intended to automate applications or replace human decision making. Its purpose is to improve the quality and consistency of career-related decisions through structured workflows and supervised AI assistance.
