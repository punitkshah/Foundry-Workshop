from __future__ import annotations

import asyncio
import os
from typing import Any

from agent_framework import Agent
from agent_framework.orchestrations import ConcurrentBuilder
from agent_framework_foundry_hosting import ResponsesHostServer
from dotenv import load_dotenv

from foundry_client import build_client
from operations_agent import build_operations_agent
from passenger_agent import build_passenger_agent

DEFAULT_REQUEST = (
    "Flight CA123 has been delayed by 2 hours due to severe weather. "
    "What actions should Contoso Air take?"
)


def build_orchestrator_agent() -> Any:
    client = build_client()
    operations = build_operations_agent(client)
    passenger = build_passenger_agent(client)
    consolidator = Agent(
        client=client,
        name="DisruptionOrchestrator",
        description="Combines specialist findings into a single response plan.",
        instructions=(
            "You are the Contoso Air Orchestrator Agent. "
            "Combine only the findings provided by the specialist agents. "
            "Do not introduce new policy or unsupported commitments. "
            "Return these sections exactly: Operational Actions, Passenger Actions, "
            "Recommended Response Plan, Immediate Next 30 Minutes."
        ),
    )

    async def aggregate(results: list[Any]) -> str:
        sections: list[str] = []
        for result in results:
            agent_response = getattr(result, "agent_response", None)
            messages = getattr(agent_response, "messages", []) or []
            final_text = getattr(messages[-1], "text", "") if messages else ""
            sections.append(
                f"{getattr(result, 'executor_id', 'specialist')}:\n{final_text}"
            )
        prompt = (
            "Consolidate these specialist findings into a single action plan:\n\n"
            + "\n\n".join(sections)
        )
        response = await consolidator.run(prompt)
        return str(response)

    workflow = (
        ConcurrentBuilder(participants=[operations, passenger])
        .with_aggregator(aggregate)
        .build()
    )
    return workflow.as_agent(
        name="contoso-air-disruption-orchestrator",
        description="Concurrent operations and passenger service orchestration for flight disruptions.",
    )


async def run_local() -> None:
    agent = build_orchestrator_agent()
    prompt = os.getenv("SAMPLE_REQUEST", DEFAULT_REQUEST)
    response = await agent.run(prompt)
    print(str(response))


def main() -> None:
    load_dotenv()
    mode = os.getenv("RUN_MODE", "local").lower()
    agent = build_orchestrator_agent()

    if mode == "host":
        port = int(os.environ.get("PORT", "8088"))
        ResponsesHostServer(agent).run(port=port)
        return

    asyncio.run(run_local())


if __name__ == "__main__":
    main()
