from explainer.prompts import (
    SOLUTIONS_ARCHITECT_SYSTEM_PROMPT,
    ANALOGY_EXPERT_SYSTEM_PROMPT,
    INFORMATION_EXPLAINER_SYSTEM_PROMPT,
    INFORMATION_SUMMARIZER_SYSTEM_PROMPT,
)
from explainer.service.config import get_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_handoff_tool, create_swarm

model = get_chat_model()

transfer_to_architect = create_handoff_tool(
    agent_name="solutions_architect",
    description="Hand control to the Solutions Architect for code-level explanations.",
)
transfer_to_analogy = create_handoff_tool(
    agent_name="analogy_expert",
    description="Hand control to the Analogy Expert for analogies.",
)
transfer_to_explainer = create_handoff_tool(
    agent_name="information_explainer",
    description="Hand control to the Information Explainer for detailed breakdowns.",
)
transfer_to_summarizer = create_handoff_tool(
    agent_name="information_summarizer",
    description="Hand control to the Information Summarizer for TL;DRs.",
)

solutions_architect = create_react_agent(
    model,
    prompt=SOLUTIONS_ARCHITECT_SYSTEM_PROMPT,
    tools=[transfer_to_analogy, transfer_to_explainer, transfer_to_summarizer],
    name="solutions_architect",
)

analogy_expert = create_react_agent(
    model,
    prompt=ANALOGY_EXPERT_SYSTEM_PROMPT,
    tools=[transfer_to_architect, transfer_to_explainer, transfer_to_summarizer],
    name="analogy_expert",
)

information_explainer = create_react_agent(
    model,
    prompt=INFORMATION_EXPLAINER_SYSTEM_PROMPT,
    tools=[transfer_to_architect, transfer_to_analogy, transfer_to_summarizer],
    name="information_explainer",
)

information_summarizer = create_react_agent(
    model,
    prompt=INFORMATION_SUMMARIZER_SYSTEM_PROMPT,
    tools=[transfer_to_architect, transfer_to_analogy, transfer_to_explainer],
    name="information_summarizer",
)

agent_swarm = create_swarm(
    [
        solutions_architect,
        analogy_expert,
        information_explainer,
        information_summarizer,
    ],
    default_active_agent="information_explainer",
)

app = agent_swarm.compile()
