# Lab 2 Solution - Contoso Air Disruption Management Multi-Agent System

This solution uses Microsoft Agent Framework to build a simple multi-agent system for airline disruption handling.

## Files

- `foundry_client.py` - Shared helper that builds the Foundry chat client
- `operations_agent.py` - Specialist agent for operational procedures
- `passenger_agent.py` - Specialist agent for passenger services
- `orchestrator_agent.py` - Concurrent orchestration and hosted deployment entry point
- `consume_agent.py` - Python client for the deployed hosted agent
- `operations_manual.md` - Operations knowledge source
- `passenger_guidelines.md` - Passenger services knowledge source
- `evaluation_data/` - Sample evaluation datasets
- `requirements.txt` - Python dependencies
- `.env.sample` - Environment variables for local run and deployed consumption

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env
```

## Test the Specialist Agents Individually

```bash
python operations_agent.py
python passenger_agent.py
```

## Local Run

```bash
RUN_MODE=local python orchestrator_agent.py
```

## Hosted Mode

Deploy `orchestrator_agent.py` as a Foundry hosted agent using the Responses protocol.

The script supports hosted execution because it exposes a `ResponsesHostServer` entry point.

## Consume the Deployed Agent

```bash
python consume_agent.py --prompt "Flight CA123 has been delayed by 2 hours due to severe weather. What actions should Contoso Air take?"
```

## Evaluation Assets

Use the sample JSONL files in `evaluation_data` when demonstrating evaluation setup.

## Sample Expected Outcome

A strong result contains four sections:

- Operational Actions
- Passenger Actions
- Recommended Response Plan
- Immediate Next 30 Minutes
