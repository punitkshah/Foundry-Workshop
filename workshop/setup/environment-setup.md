# Environment Setup

This setup keeps infrastructure to a minimum. Participants only need Foundry access, Azure sign-in, and local Python.

## 1. Sign in to Azure

```bash
az login
az account show
```

If you use multiple subscriptions, set the intended one explicitly:

```bash
az account set --subscription "<your-subscription-name-or-id>"
```

## 2. Create a Local Python Environment

Create separate virtual environments for each lab so troubleshooting stays simple.

### Lab 1

From the workshop root folder:

```bash
cd workshop/lab1-flight-delay-communications/solution
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` instead of `source .venv/bin/activate`.

### Lab 2

From the workshop root folder:

```bash
cd workshop/lab2-disruption-management/solution
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` instead of `source .venv/bin/activate`.

## 3. Create Environment Files

Copy each sample environment file and populate it with your project values.

### Lab 1

```bash
cp .env.sample .env
```

### Lab 2

```bash
cp .env.sample .env
```

## 4. Required Environment Values

### Lab 1

Populate:

- `PROJECT_ENDPOINT`
- `AGENT_ID`

### Lab 2

Populate:

- `FOUNDRY_PROJECT_ENDPOINT`
- `FOUNDRY_MODEL`
- `AZURE_AI_PROJECT_ENDPOINT`
- `HOSTED_AGENT_NAME`

## 5. Validate the Environment

### Lab 1 validation

```bash
python consume_agent.py --flight-number CA123 --delay-reason Weather --delay-duration "2 hours"
```

### Lab 2 local validation

```bash
RUN_MODE=local python orchestrator_agent.py
```

### Lab 2 deployed validation

```bash
python consume_agent.py --prompt "Flight CA123 has been delayed by 2 hours due to severe weather. What actions should Contoso Air take?"
```

## 6. Troubleshooting Tips

- If authentication fails, run `az login` again and verify tenant context.
- If Python package installation fails, upgrade pip first: `python -m pip install --upgrade pip`.
- If a deployment is not visible, refresh the Foundry project page and confirm the correct project endpoint.
