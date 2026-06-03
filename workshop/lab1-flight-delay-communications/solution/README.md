# Lab 1 Solution - Consume the Delay Communications Agent

This folder contains a Python sample that calls the deployed Contoso Air prompt agent from Microsoft Foundry.

## Files

- `consume_agent.py` - Python client for invoking the deployed agent
- `requirements.txt` - Python dependencies
- `.env.sample` - Environment variables to copy into `.env`
- `evaluation_dataset.jsonl` - Sample evaluation dataset for Lab 1

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env
```

Populate `.env`:

- `PROJECT_ENDPOINT`: Foundry project endpoint
- `AGENT_ID`: The deployed prompt agent ID

## Run

```bash
python consume_agent.py --flight-number CA123 --delay-reason Weather --delay-duration "2 hours"
```

You can also pass a custom prompt directly:

```bash
python consume_agent.py --message "Flight Number: CA456
Delay Reason: Technical inspection
Delay Duration: 45 minutes"
```

## What the Script Does

1. Authenticates with `DefaultAzureCredential`
2. Connects to the Foundry project
3. Creates a thread
4. Sends a user prompt
5. Runs the deployed agent
6. Prints the assistant response
7. Surfaces useful error messages if the run fails

## Expected Outcome

A successful run prints content with three sections:

- Airport Announcement
- SMS Message
- Email Communication

## Common Errors

### `DefaultAzureCredential failed`

Run `az login` and confirm that you can access the workshop subscription.

### `Run failed`

Verify that `AGENT_ID` points to the correct deployed agent version.

### Empty or incomplete output

Check whether the deployed agent instructions still require all three communication formats.
