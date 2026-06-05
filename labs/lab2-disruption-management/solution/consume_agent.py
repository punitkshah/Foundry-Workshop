from __future__ import annotations

import argparse
import os
import sys
import urllib.parse

import requests
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

DEFAULT_PROMPT = (
    "Flight CA123 has been delayed by 2 hours due to severe weather. "
    "What actions should DP World take?"
)
API_VERSION = "2025-11-15-preview"
SCOPE = "https://ai.azure.com/.default"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Call the deployed DP World hosted orchestrator.")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT)
    return parser.parse_args()


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def get_token() -> str:
    credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    return credential.get_token(SCOPE).token


def extract_output_text(payload: dict) -> str:
    output = payload.get("output", [])
    snippets: list[str] = []
    for item in output:
        for content in item.get("content", []):
            text = content.get("text")
            if text:
                snippets.append(text)
    return "\n".join(snippets).strip()


def main() -> int:
    load_dotenv()
    args = parse_args()

    try:
        endpoint = require_env("AZURE_AI_PROJECT_ENDPOINT").rstrip("/")
        agent_name = require_env("HOSTED_AGENT_NAME")
        agent_path = urllib.parse.quote(agent_name, safe="")
        token = get_token()
        headers = {
            "Authorization": f"******",
            "Content-Type": "application/json",
            "x-ms-protocol-version": "1.0.0",
            "x-ms-agent-protocol-version": "1.0.0",
        }
        payload = {"input": [{"role": "user", "content": args.prompt}]}
        url = (
            f"{endpoint}/agents/{agent_path}/endpoint/protocols/openai/responses"
            f"?api-version={API_VERSION}"
        )
        response = requests.post(url, headers=headers, json=payload, timeout=180)
        if not response.ok:
            raise RuntimeError(f"HTTP {response.status_code}: {response.text[:500]}")
        response_text = extract_output_text(response.json())
        print(response_text or response.text)
        return 0
    except Exception as exc:  # noqa: BLE001 - concise workshop errors
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
