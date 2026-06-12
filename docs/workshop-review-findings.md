# Workshop Validation and Optimization — Findings Report

This report captures the end-to-end review of the Foundry workshop performed against the success
criteria in [issue #12](https://github.com/punitkshah/Foundry-Workshop/issues/12). Findings are
listed first, followed by the changes made in this pull request, time analysis, and remaining
recommendations.

## 1. Findings Report

| Severity | Finding | Impact | Fix in this PR |
|---|---|---|---|
| **Critical** | `labs/lab2-disruption-management/solution/consume_agent.py` (and its mirror in `lab-guide.md` Part 13) set `Authorization` to a literal asterisks string instead of `Bearer <token>` | Every call to the deployed hosted orchestrator returns HTTP 401. Lab 2 cannot be completed end-to-end as written. | Replaced the literal with `f"Bearer {token}"` in both the solution script and the lab guide. |
| **High** | Workshop duration was inconsistent across documents: `README.md` showed 2:35, `docs/workshop-agenda.md` said "approximately 2.5 hours", `instructor-guide/timing.md` said "150 Minutes", `labs/lab2-disruption-management/lab-guide.md` claimed "90–120 minutes" for Lab 2 alone, while the Lab 2 README said "60–75 minutes". The issue requires the workshop fit in **90 minutes**. | Participants and instructors get a different time budget from every document; the workshop cannot be planned reliably. | Realigned **all six** documents to a single coherent 90-minute plan (Intro 5 / Lab 1 35 / Lab 2 45 / Wrap-up 5). |
| **High** | Lab 2 (14 parts) requires participants to hand-type six Python files and three JSONL evaluation files from the guide. This cannot fit any plausible 45-minute live budget. | The lab either over-runs or skips the orchestration/deployment concepts that are the actual learning objective. | Added a **Workshop Mode (90-minute path)** section to the Lab 2 guide and Lab 2 README. In Workshop Mode participants run the prebuilt code in `solution/` and read the guide as a walkthrough; the **Self-Paced Build-From-Scratch Mode** is preserved unchanged for learners outside a live session. Instructor timing guide now explicitly assumes Workshop Mode. |
| **Medium** | Prerequisites and Environment Setup were listed as in-session steps (10 + 15 min), which is unrealistic when the total live budget is 90 minutes. | ~25 minutes of live time would have been spent on `az login` and `pip install`, leaving the hands-on labs starved. | Workshop Navigation in `README.md`, the agenda, and the instructor timing guide now mark Prerequisites and Environment Setup as **before-the-session** steps. |
| **Low** | No CI/lint configuration exists in the repository, so the broken `Authorization` header was not caught automatically. | Future regressions in the Python clients can ship undetected. | Out of scope for this PR; see *Remaining Recommendations* below. |

## 2. Changes Made in This Pull Request

### Code fixes
- `labs/lab2-disruption-management/solution/consume_agent.py` — fixed the `Authorization` header so authenticated calls to the deployed orchestrator succeed.
- `labs/lab2-disruption-management/lab-guide.md` (Part 13) — same fix in the printed code so participants who hand-type from the guide also get a working script.

### Documentation alignment (single 90-minute plan)
- `README.md` — Workshop Navigation table and Agenda table updated; Prerequisites/Setup marked as pre-work.
- `docs/workshop-agenda.md` — full agenda rewritten for the 90-minute slot.
- `instructor-guide/timing.md` — instructor agenda rewritten with per-part minute budgets and explicit "Workshop Mode" guidance for Lab 2.
- `labs/lab1-flight-delay-communications/README.md` and `labs/lab1-flight-delay-communications/lab-guide.md` — duration updated to "35 minutes in a live workshop; 45–60 minutes self-paced".
- `labs/lab2-disruption-management/README.md` and `labs/lab2-disruption-management/lab-guide.md` — duration banner and "Choose Your Mode" section added (Workshop Mode = 45 min using `solution/`; Self-Paced Mode = 90–120 min building from scratch).

### Net effect for a workshop participant
- Lab 2 now works end-to-end (Part 13 no longer returns 401).
- A participant who reads any of `README.md`, `docs/workshop-agenda.md`, `instructor-guide/timing.md`, or either lab's README/lab-guide sees the **same** 90-minute plan.
- Lab 2 is realistically executable within its allotted 45 minutes via Workshop Mode without losing the deep self-paced track for learners who want to build from scratch.

## 3. Time Analysis

### Live 90-minute workshop (Workshop Mode for Lab 2)

| Segment | Estimated Time | Notes |
|---|---|---|
| Introduction & architecture overview | 5 min | Contoso Air scenario + Build→Evaluate→Deploy→Consume lifecycle. |
| Lab 1 – Flight Delay Communications Assistant | 35 min | Foundry portal flow: project, prompt agent, prompt iteration (Part 6), one eval run discussion, deploy, Python consumption with `solution/consume_agent.py`. Eval re-run (Part 9) can be discussed verbally if time is tight. |
| Lab 2 – Disruption Management Multi-Agent System | 45 min | Workshop Mode: run `operations_agent.py`, `passenger_agent.py`, then `orchestrator_agent.py`; walk through `aggregate` + `ConcurrentBuilder`; discuss the three evaluation datasets; instructor-demo the hosted deployment; run `consume_agent.py` against the deployed endpoint. |
| Wrap-up & Q&A | 5 min | Architecture-evolution discussion prompts from the [Answer Key](../instructor-guide/answer-key.md). |
| **Total** | **90 min** | Matches the success criterion in issue #12. |

### Self-paced execution (full Build-From-Scratch Mode)

| Lab | Estimated Time | Notes |
|---|---|---|
| Lab 1 | 45–60 min | Includes prompt iteration loop and second evaluation run. |
| Lab 2 | 90–120 min | Includes typing six Python files, three JSONL datasets, and the optional Challenge Exercise. |

### Areas most likely to slow participants down

1. Foundry portal project creation if a hub does not yet exist (Lab 1 Part 3).
2. First-time `pip install` of `agent-framework*` packages on a slow network (Lab 2 Part 3).
3. Hosted-agent deployment (Lab 2 Part 12). This step has the most variability; the timing guide
   makes it an instructor demo rather than a participant task during the 90-minute slot.

## 4. Improvement Summary

| Area | Improvement |
|---|---|
| Documentation | Single, coherent 90-minute plan across README, agenda, instructor guide, and both lab READMEs/guides. Prerequisites and Environment Setup explicitly framed as before-session work. |
| Repository structure | No restructure required. The current layout (`docs/`, `labs/<lab>/{README, lab-guide, starter-code, solution}/`, `instructor-guide/`, `slides/`) is already intuitive and well-suited to the lifecycle theme, so changing it would only invalidate links without adding clarity. |
| Lab flow | Lab 2 now offers two clearly labeled modes (Workshop, Self-Paced). Self-Paced learners keep the full hands-on experience; live participants can complete the lab within the time budget. |
| Learning experience | The fix to `consume_agent.py` removes the most common participant blocker (silent 401s on Part 13). The Lab 2 "Choose Your Mode" section sets expectations up front, reducing perceived ambiguity. |
| Starter code & boilerplate | The `solution/` folder is now the recommended live-workshop entry point for Lab 2, eliminating ~30 min of unnecessary typing. No code-content changes were required because the existing solution scripts were already self-contained and runnable; only the broken header needed fixing. |
| Workshop timing | Realigned to a realistic 90-minute live agenda with explicit per-part budgets in `instructor-guide/timing.md`. |

## 5. Remaining Recommendations (out of scope for this PR)

These are worth doing but were intentionally not included to keep this PR surgical:

- **Add lightweight CI** (`python -m py_compile` over the two `consume_agent.py` files, plus `pip install --dry-run` for both `requirements.txt` files) so that a regression like the broken `Authorization` header is caught automatically.
- **Capture real screenshots** to replace the `[Insert Screenshot – …]` and `🖼️ Screenshot placeholder` markers in both lab guides. They are not required to complete the labs, but they would improve the customer-facing polish.
- **Pin `requirements.txt` versions** for the workshop. Today both files use `>=` constraints; pinning to known-good versions reduces "works on my machine" issues during live sessions.
- **Add a 5-minute "Sanity Check" script** to `solution/` for each lab that verifies `.env` is populated and that `az login` is valid before participants start the lab, so misconfigured environments fail fast.
