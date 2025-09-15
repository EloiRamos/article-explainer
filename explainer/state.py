from langgraph.graph import MessagesState

class ExplainerState(MessagesState):
    """State schema for the multi-agent swarm."""

    """Notion of the agent that is actively handling the user request."""
    active_agent: str | None

    """Obtained content from the source document"""
    document_content: str