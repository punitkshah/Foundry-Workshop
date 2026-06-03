from __future__ import annotations

from pathlib import Path

from agent_framework import Agent


SYSTEM_PROMPT = """You are the Contoso Air Operations Agent.

Use only the operations manual provided in your instructions.
Return operational guidance for airline staff, not passenger copy.
Always organize your answer as:
- Operational Actions
- Operational Risks
- Escalations
Do not invent policies that are not in the manual.
"""


def build_operations_agent(client, manual_path: str | None = None) -> Agent:
    path = Path(manual_path or Path(__file__).with_name("operations_manual.md"))
    manual = path.read_text(encoding="utf-8")
    return Agent(
        client=client,
        name="OperationsAgent",
        description="Specialist for operational disruption procedures.",
        instructions=f"{SYSTEM_PROMPT}\n\nOperations Manual:\n{manual}",
    )
