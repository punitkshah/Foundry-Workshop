# Lab 2 Starter Code

This folder contains the non-generated inputs for the multi-agent lab.

Use it when you want participants to author the Python files themselves during the workshop.

## Included Assets

- `operations_manual.md`
- `passenger_guidelines.md`
- `requirements.txt`
- `.env.sample`

## Suggested Exercise Flow

1. Install dependencies from `requirements.txt`.
2. Load the markdown files into agent instructions.
3. Create an Operations Agent.
4. Create a Passenger Services Agent.
5. Create an orchestrator that fans out and consolidates.
6. Promote the final code to the `solution` pattern if needed.

## Minimal Run Commands

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env
```
