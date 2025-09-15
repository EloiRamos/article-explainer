from explainer.prompts import SOLUTIONS_ARCHITECT_SYSTEM_PROMPT, ANALOGY_EXPERT_SYSTEM_PROMPT, \
    INFORMATION_EXPLAINER_SYSTEM_PROMPT, INFORMATION_SUMMARIZER_SYSTEM_PROMPT
from explainer.service.config import get_chat_model
from explainer.service.content_loader import ContentLoader
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_handoff_tool, create_swarm
from langchain_core.messages import HumanMessage
from explainer.state import ExplainerState


def build_swarm(document_summary: str):
    """Create the swarm with prompts formatted using the summary."""
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
        prompt=SOLUTIONS_ARCHITECT_SYSTEM_PROMPT.format(document_content=document_summary),
        tools=[transfer_to_analogy, transfer_to_explainer, transfer_to_summarizer],
        name="solutions_architect",
    )

    analogy_expert = create_react_agent(
        model,
        prompt=ANALOGY_EXPERT_SYSTEM_PROMPT.format(document_content=document_summary),
        tools=[transfer_to_architect, transfer_to_explainer, transfer_to_summarizer],
        name="analogy_expert",
    )

    information_explainer = create_react_agent(
        model,
        prompt=INFORMATION_EXPLAINER_SYSTEM_PROMPT.format(document_content=document_summary),
        tools=[transfer_to_architect, transfer_to_analogy, transfer_to_summarizer],
        name="information_explainer",
    )

    information_summarizer = create_react_agent(
        model,
        prompt=INFORMATION_SUMMARIZER_SYSTEM_PROMPT.format(document_content=document_summary),
        tools=[transfer_to_architect, transfer_to_analogy, transfer_to_explainer],
        name="information_summarizer",
    )

    return create_swarm(
        [
            solutions_architect,
            analogy_expert,
            information_explainer,
            information_summarizer,
        ],
        default_active_agent="information_explainer",
    )


def main():
    loader = ContentLoader()

    summary_text = loader.get_text(
        "/Users/duarte/Documents/Dev/article-explainer/article-explainer/docs/small_language_models_summary.txt",
        max_chunks=10,
    )

    agent_swarm = build_swarm(document_summary=summary_text)
    app = agent_swarm.compile()

    state = ExplainerState(
        active_agent="information_explainer",
        messages=[{"role": "user", "content": "Hi, I want to discuss the document summary."}],
        document_content=summary_text,
    )

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        state["messages"].append(HumanMessage(content=user_input))

        state = app.invoke(state)

        last_msg = state["messages"][-1]
        print("\nAssistant:", last_msg.content)

if __name__ == "__main__":
    main()
