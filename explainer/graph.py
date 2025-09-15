from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_handoff_tool, create_swarm
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4.1-mini")

transfer_to_architect = create_handoff_tool(
    agent_name="solutions_architect",
    description="Hand control to the Solutions Architect when code-level or technical details are needed.",
)

transfer_to_analogy = create_handoff_tool(
    agent_name="analogy_expert",
    description="Hand control to the Analogy Expert when analogies are useful for better understanding.",
)

transfer_to_explainer = create_handoff_tool(
    agent_name="information_explainer",
    description="Hand control to the Information Explainer for breaking down concepts clearly.",
)

transfer_to_summarizer = create_handoff_tool(
    agent_name="information_summarizer",
    description="Hand control to the Information Summarizer for concise overviews and TL;DR outputs.",
)

solutions_architect = create_react_agent(
    model,
    prompt="""
    You are the Solutions Architect.
    Your job is to explain the information in code-level or technical detail.
    Provide code snippets, structured pseudo-code, or step-by-step technical breakdowns.
    """,
    tools=[transfer_to_analogy, transfer_to_explainer, transfer_to_summarizer],
    name="solutions_architect",
)

analogy_expert = create_react_agent(
    model,
    prompt="""
    You are the Analogy Expert.
    Your job is to explain complex concepts using clear, relatable analogies.
    Use real-world examples that help simplify understanding for non-technical audiences.
    """,
    tools=[transfer_to_architect, transfer_to_explainer, transfer_to_summarizer],
    name="analogy_expert",
)

information_explainer = create_react_agent(
    model,
    prompt="""
    You are the Information Explainer.
    Your job is to break down content into clear, structured explanations step by step.
    Think of yourself as a teacher who ensures the material is understandable.
    """,
    tools=[transfer_to_architect, transfer_to_analogy, transfer_to_summarizer],
    name="information_explainer",
)

information_summarizer = create_react_agent(
    model,
    prompt="""
    You are the Information Summarizer.
    Your job is to condense the content into a short, clear TL;DR.
    Keep it concise and highlight only the most important points.
    """,
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
