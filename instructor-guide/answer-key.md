# Instructor Answer Key

## Lab 1 Key Takeaways

A successful Lab 1 solution should show:

- A prompt agent named `contoso-air-delay-comms`
- Strong instruction scaffolding for empathy, structure, and no-invention behavior
- An evaluation dataset with multiple disruption scenarios
- A deployed version consumed from Python using Foundry project credentials

## Lab 1 High-Value Improvement

If participants struggle, the most useful prompt refinement is:

- Explicit output headings
- Explicit SMS length limit
- Explicit ban on inventing compensation, vouchers, or rebooking promises

## Lab 2 Key Takeaways

A successful Lab 2 solution should show:

- One specialist agent for operations
- One specialist agent for passenger services
- One orchestrator that combines both outputs
- Local markdown files used as the knowledge source
- Only the orchestrator deployed as the customer-facing endpoint

## Expected Strong Orchestrator Behavior

The orchestrator should:

- Include both operations and passenger sections
- Avoid policy invention
- Provide a short-term action plan
- Resolve conflicts by staying grounded in specialist content

## Discussion Prompt for Wrap-Up

Ask participants:

- When is a prompt agent sufficient?
- When does decomposition into specialists improve reliability?
- Which evaluation metrics helped the most in finding weaknesses?
