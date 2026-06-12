# Lab 2 – Disruption Management Multi-Agent System

Build a **multi-agent solution** for Contoso Air with the **Microsoft Agent Framework**: two specialist
agents coordinated by an orchestrator that consolidates their findings into a single action plan.

> **Lifecycle focus:** **Build → Evaluate → Deploy → Consume**

---

## Lab Navigation

- **Previous:** [Lab 1 – Flight Delay Communications Assistant](../lab1-flight-delay-communications/README.md)
- **Next:** [Workshop Wrap-Up](../../README.md#wrap-up)
- **Up:** [Workshop Home](../../README.md)

---

## Estimated Duration

45 minutes in **Workshop Mode** (using the prebuilt `solution/` code; see the note at the top of
the [lab guide](lab-guide.md)). Allow 90–120 minutes for the full self-paced **Build-From-Scratch
Mode** in which you type every file yourself.

## Lab Objectives

By the end of this lab, you will be able to:

- Create agents with the Microsoft Agent Framework
- Build specialist agents grounded in local knowledge files
- Build an orchestrator that coordinates the specialists
- Test the system locally and evaluate each agent tier
- Deploy the orchestrator and consume it from Python

## Prerequisites

- Completed [Lab 1](../lab1-flight-delay-communications/README.md)
- Completed the [Environment Setup](../../docs/environment-setup.md)
- Active Azure sign-in with access to a Foundry project and model deployment

## What's in This Lab

- **[lab-guide.md](lab-guide.md)** – a complete, self-contained hands-on workshop. It includes every
  command and every line of code, so you can build the whole solution from an empty folder **without
  opening the solution folder**.
- **[starter-code/](starter-code/)** – knowledge files and dependencies if you prefer to start from a
  scaffold instead of typing the knowledge files from the guide
- **[solution/](solution/)** – the reference implementation (specialist agents, orchestrator,
  evaluation datasets, and client) for comparison if you get stuck

## Validation Checkpoints

You should be able to demonstrate:

- Two specialist agents grounded in local markdown files
- An orchestrator that consolidates both outputs
- A successful local test
- Evaluation datasets for each agent tier
- A deployed orchestrator endpoint
- Successful Python consumption of the deployed endpoint

## Need the Solution?

Try building the agents from the [starter-code/](starter-code/) first. If you get stuck, the reference
implementation is in [solution/](solution/) with its own [README](solution/README.md).

---

➡️ **Start the lab: [Lab 2 Guide](lab-guide.md)**
