# Instructor Timing Guide

## Suggested Agenda (90 Minutes)

The workshop is designed for a tight **90-minute** live session. **Prerequisites and environment
setup are completed by participants before the session** (see [Prerequisites](../docs/prerequisites.md)
and [Environment Setup](../docs/environment-setup.md)). All live time is spent on the labs and discussion.

### 0:00–0:05 — Introduction

- Introduce Contoso Air scenario
- Explain Build -> Evaluate -> Deploy -> Consume
- Contrast prompt agents and multi-agent systems

### 0:05–0:40 — Lab 1 (35 min)

- 5 min: Create Foundry project and agent (Parts 3–4)
- 10 min: Test prompts and iterate on instructions (Parts 5–6)
- 10 min: Evaluation walkthrough (Parts 7–9, demo the second run if time is tight)
- 5 min: Deployment (Parts 10–11)
- 5 min: Python consumption from `solution/consume_agent.py` (Parts 12–13)

### 0:40–1:25 — Lab 2 (45 min)

Run Lab 2 in **Workshop Mode**: participants use the prebuilt code in
`labs/lab2-disruption-management/solution/` instead of typing every file. Live focus is on
**concepts** — grounding, orchestration, evaluation, and hosted deployment.

- 5 min: Review the multi-agent architecture and scenario (Part 1)
- 10 min: Run each specialist agent and inspect grounded answers (Parts 5–7)
- 10 min: Walk through `orchestrator_agent.py` and run end-to-end locally (Parts 8–9)
- 5 min: Evaluation datasets and metrics discussion (Part 11)
- 10 min: Hosted deployment walkthrough (Parts 10, 12 — instructor demo)
- 5 min: Python consumption of the deployed orchestrator (Part 13)

### 1:25–1:30 — Wrap-up and Q&A

- Revisit the architecture evolution
- Discuss production considerations
- Answer participant questions

## Instructor Tips

- Keep Lab 1 crisp; it establishes confidence quickly. Demo the second evaluation run if time is short.
- Lab 2 fits **only** when participants run the prebuilt `solution/` code. Do not have them type the
  six Python files in a 90-minute slot — point to the lab guide's optional **Self-Paced Mode** instead.
- Spend more time on orchestration decisions than on syntax in Lab 2.
- Use the evaluation discussion to connect architecture with measurable quality.
- The optional Challenge Exercise at the end of each lab is for self-paced follow-up, not live time.
