from langchain_ollama import ChatOllama
from langchain.chat_models import init_chat_model
from config.settings import settings

def get_chat_model(model_name: str = None):
    ""Returns a LangChain chat model initialized with the API key from settings."""
    if model_name is None:
        model_name = settings.openai_model

    if settings.openai_api_key:
        return init_chat_model(model=model_name, api_key=settings.openai_api_key)
    else:
        # Fallback to Ollama for local development
        return ChatOllama(
            model=settings.ollama_model,
            base_url=settings.ollama_base_url
        )