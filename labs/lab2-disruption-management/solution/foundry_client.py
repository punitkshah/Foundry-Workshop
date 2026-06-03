from __future__ import annotations

import os

from agent_framework.foundry import FoundryChatClient
from azure.identity import DefaultAzureCredential


def build_client() -> FoundryChatClient:
    """Create a Foundry chat client from environment variables.

    Requires FOUNDRY_PROJECT_ENDPOINT and FOUNDRY_MODEL to be set.
    """
    endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    model = os.environ["FOUNDRY_MODEL"]
    credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    return FoundryChatClient(
        project_endpoint=endpoint,
        model=model,
        credential=credential,
    )
