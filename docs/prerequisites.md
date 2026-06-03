# Prerequisites

Use this checklist before the workshop starts.

## Required Access

Participants need:

- An Azure subscription that allows Microsoft Foundry usage
- Permission to create or use a Microsoft Foundry project
- Access to at least one chat-capable model deployment in the project
- Permission to deploy agent versions in the project

Recommended project roles:

- Azure AI Developer or equivalent project-level contributor access
- Rights to view deployments, evaluation runs, and endpoint details

## Local Tools

Install the following before the session:

- Python 3.10 or later
- Azure CLI (`az`)
- Visual Studio Code or another Python editor
- Git

Optional but helpful:

- Microsoft Foundry Toolkit for Visual Studio Code
- `curl` or Postman for quick endpoint testing

## Python Packages Used in the Workshop

Lab 1 uses:

- `azure-ai-projects`
- `azure-ai-agents`
- `azure-identity`
- `python-dotenv`

Lab 2 uses:

- `agent-framework`
- `agent-framework-foundry`
- `agent-framework-foundry-hosting`
- `azure-identity`
- `python-dotenv`
- `requests`

## Foundry Setup Checklist

Before the hands-on portion, confirm that each participant has:

- A Foundry project endpoint
- A model deployment name for the workshop model
- Successful sign-in with `az login`
- Network access to Foundry and Azure authentication endpoints

## Minimum Model Guidance

Any chat-capable model can be used, but the workshop runs best with:

- A general-purpose model for prompt-based generation in Lab 1
- The same or another general-purpose model for specialist and orchestrator agents in Lab 2

## Pre-Flight Validation

Ask participants to verify:

```bash
az login
az account show
python --version
```

Expected result:

- Azure CLI is authenticated
- Python is available
- The participant can identify the subscription and tenant they will use
