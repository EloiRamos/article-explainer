import pytest
import os
from unittest.mock import patch


@pytest.fixture
def mock_env_openai():
    """Mock environment with OpenAI API key."""
    with patch.dict(os.environ, {"OPENAI_API_KEY": "test-key"}):
        yield


@pytest.fixture
def mock_env_ollama():
    """Mock environment with Ollama configuration."""
    with patch.dict(os.environ, {
        "OLLAMA_BASE_URL": "http://localhost:11434",
        "OLLAMA_MODEL": "test-model"
    }):
        yield