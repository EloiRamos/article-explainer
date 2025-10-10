from explainer.prompts import (
    PLANNER_SYSTEM_PROMPT,
    DEVELOPER_SYSTEM_PROMPT,
    SUMMARIZER_SYSTEM_PROMPT,
    EXPLAINER_SYSTEM_PROMPT,
    ANALOGY_CREATOR_SYSTEM_PROMPT,
    VULNERABILITY_EXPERT_SYSTEM_PROMPT,
)
from explainer.service.config import get_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_handoff_tool, create_swarm

model = get_chat_model()

transfer_to_planner = create_handoff_tool(
    agent_name="planner",
    description="Hand control back to the Planner for coordination and final report generation.",
)
transfer_to_developer = create_handoff_tool(
    agent_name="developer",
    description="Hand control to the Developer for code examples and technical implementations.",
)
transfer_to_summarizer = create_handoff_tool(
    agent_name="summarizer",
    description="Hand control to the Summarizer for concise summaries, key points, and TL;DR responses.",
)
transfer_to_explainer = create_handoff_tool(
    agent_name="explainer",
    description="Hand control to the Explainer for detailed step-by-step breakdowns and educational explanations.",
)
transfer_to_analogy_creator = create_handoff_tool(
    agent_name="analogy_creator",
    description="Hand control to the Analogy Creator for creating relatable analogies and metaphors for complex concepts.",
)
transfer_to_vulnerability_expert = create_handoff_tool(
    agent_name="vulnerability_expert",
    description="Hand control to the Vulnerability Expert for analyzing potential weaknesses in arguments and methodology.",
)

# Create agents with needed tools and handoff capabilities
planner = create_react_agent(
    model,
    prompt=PLANNER_SYSTEM_PROMPT,
    tools=[
        transfer_to_developer,
        transfer_to_summarizer,
        transfer_to_explainer,
        transfer_to_analogy_creator,
        transfer_to_vulnerability_expert,
    ],
    name="planner",
)

developer = create_react_agent(
    model,
    prompt=DEVELOPER_SYSTEM_PROMPT,
    tools=[
        transfer_to_planner,
    ],
    name="developer",
)

summarizer = create_react_agent(
    model,
    prompt=SUMMARIZER_SYSTEM_PROMPT,
    tools=[
        transfer_to_planner,
    ],
    name="summarizer",
)

explainer = create_react_agent(
    model,
    prompt=EXPLAINER_SYSTEM_PROMPT,
    tools=[
        transfer_to_planner,
    ],
    name="explainer",
)

analogy_creator = create_react_agent(
    model,
    prompt=ANALOGY_CREATOR_SYSTEM_PROMPT,
    tools=[
        transfer_to_planner,
    ],
    name="analogy_creator",
)

vulnerability_expert = create_react_agent(
    model,
    prompt=VULNERABILITY_EXPERT_SYSTEM_PROMPT,
    tools=[
        transfer_to_planner,
    ],
    name="vulnerability_expert",
)

agent_swarm = create_swarm(
    [
        planner,
        developer,
        summarizer,
        explainer,
        analogy_creator,
        vulnerability_expert,
    ],
    default_active_agent="planner",
)

app = agent_swarm.compile()
