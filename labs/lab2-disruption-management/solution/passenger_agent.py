from __future__ import annotations

import asyncio
from pathlib import Path

from agent_framework import Agent
from dotenv import load_dotenv

from foundry_client import build_client


SYSTEM_PROMPT = """You are the DP World Passenger Services Agent.

Use only the passenger service guidance provided in your instructions.
Return actionable guidance for frontline service teams.
Always organize your answer as:
- Passenger Actions
- Communication Guidance
- Service Recovery Notes
Do not invent entitlements, compensation, or hotel approvals.
"""


def build_passenger_agent(client, guidelines_path: str | None = None) -> Agent:
    path = Path(guidelines_path or Path(__file__).with_name("passenger_guidelines.md"))
    guidelines = path.read_text(encoding="utf-8")
    return Agent(
        client=client,
        name="PassengerServicesAgent",
        description="Specialist for passenger communication and service recovery.",
        instructions=f"{SYSTEM_PROMPT}\n\nPassenger Services Guidelines:\n{guidelines}",
    )


async def _demo() -> None:
    load_dotenv()
    client = build_client()
    agent = build_passenger_agent(client)
    prompt = (
        "Flight CA123 is delayed by 2 hours due to severe weather. "
        "What passenger actions are required?"
    )
    response = await agent.run(prompt)
    print(str(response))


if __name__ == "__main__":
    asyncio.run(_demo())
