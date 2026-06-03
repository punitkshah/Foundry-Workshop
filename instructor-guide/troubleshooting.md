# Troubleshooting Guide

## General Issues

### Azure sign-in problems

Symptoms:

- `DefaultAzureCredential` fails
- Endpoint requests return 401 or 403

Fixes:

- Run `az login`
- Confirm the correct subscription with `az account show`
- Ensure the participant has access to the Foundry project

## Lab 1 Issues

### Prompt agent output is missing one section

Cause:

- The instructions do not strongly enforce the response structure

Fix:

- Add explicit format headings and re-test

### The agent mentions compensation or rebooking when not asked

Cause:

- The prompt is too permissive

Fix:

- Add a rule that the agent must not invent compensation, vouchers, or policy decisions

## Lab 2 Issues

### Specialist agents return generic answers

Cause:

- The knowledge file was not included clearly in the instructions

Fix:

- Load the markdown file contents directly into each specialist's instructions

### The orchestrator hallucinates policy

Cause:

- The consolidation step is not grounded tightly enough

Fix:

- Tell the consolidator to use only specialist findings and avoid unsupported promises

### Hosted agent deploys but invocation fails

Cause:

- Wrong project endpoint, missing environment variables, or incorrect agent name

Fix:

- Verify `AZURE_AI_PROJECT_ENDPOINT`
- Verify `HOSTED_AGENT_NAME`
- Confirm the deployment status in Foundry

### Responses endpoint returns an empty body

Cause:

- The response payload parsing is wrong or the agent produced a different schema

Fix:

- Inspect the raw JSON response
- Confirm the deployment is using the OpenAI responses protocol
