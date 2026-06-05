from __future__ import annotations

import argparse
import os
import sys
from typing import Iterable

from azure.ai.agents.models import MessageRole
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Invoke the deployed DP World flight delay communications agent."
    )
    parser.add_argument("--flight-number", default="CA123")
    parser.add_argument("--delay-reason", default="Weather")
    parser.add_argument("--delay-duration", default="2 hours")
    parser.add_argument("--message", help="Optional raw user message to send instead of structured inputs.")
    return parser.parse_args()


def build_prompt(args: argparse.Namespace) -> str:
    if args.message:
        return args.message
    return (
        f"Flight Number: {args.flight_number}\n"
        f"Delay Reason: {args.delay_reason}\n"
        f"Delay Duration: {args.delay_duration}\n\n"
        "Generate an Airport Announcement, SMS Message, and Email Communication."
    )


def extract_text_fragments(message) -> Iterable[str]:
    content = getattr(message, "content", None) or []
    for item in content:
        if isinstance(item, dict):
            if item.get("type") == "text":
                text_value = item.get("text", {})
                if isinstance(text_value, dict):
                    value = text_value.get("value")
                    if value:
                        yield value
                elif text_value:
                    yield str(text_value)
        else:
            item_type = getattr(item, "type", None)
            if item_type == "text":
                text_value = getattr(item, "text", None)
                value = getattr(text_value, "value", None) if text_value else None
                if value:
                    yield value


def first_assistant_message(messages) -> object | None:
    for message in getattr(messages, "data", messages):
        role = str(getattr(message, "role", "")).lower()
        if role.endswith("assistant") or role == "assistant":
            return message
    return None


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def main() -> int:
    load_dotenv()
    args = parse_args()

    try:
        endpoint = require_env("PROJECT_ENDPOINT")
        agent_id = require_env("AGENT_ID")
        credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)

        project_client = AIProjectClient(endpoint=endpoint, credential=credential)
        with project_client:
            thread = project_client.agents.threads.create()
            project_client.agents.messages.create(
                thread_id=thread.id,
                role=MessageRole.USER,
                content=build_prompt(args),
            )
            run = project_client.agents.runs.create_and_process(
                thread_id=thread.id,
                agent_id=agent_id,
            )
            if getattr(run, "status", "") == "failed":
                raise RuntimeError(f"Agent run failed: {getattr(run, 'last_error', 'Unknown error')}")

            messages = project_client.agents.messages.list(thread_id=thread.id)
            assistant_message = first_assistant_message(messages)
            if assistant_message is None:
                raise RuntimeError("The agent completed but returned no assistant message.")

            response_text = "\n".join(extract_text_fragments(assistant_message)).strip()
            if not response_text:
                raise RuntimeError("The assistant message did not contain text content.")

            print(response_text)
        return 0
    except Exception as exc:  # noqa: BLE001 - workshop-friendly error output
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
