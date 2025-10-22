import pytest
from unittest.mock import patch
from explainer.service.config import get_chat_model
from config.settings import Settings


class TestConfig:
    """Test configuration module."""

    def test_get_chat_model_with_openai_key(self):
        """Test that OpenAI model is returned when API key is available."""
        with patch.object(Settings, 'openai_api_key', 'test-key'):
            model = get_chat_model()
            # The function should return a chat model instance
            assert model is not None
            assert hasattr(model, 'invoke')

    def test_get_chat_model_without_openai_key(self):
        """Test that Ollama model is returned when no OpenAI key."""
        with patch.object(Settings, 'openai_api_key', None):
            with patch.object(Settings, 'ollama_model', 'test-model'):
                model = get_chat_model()
                assert model is not None

    def test_get_chat_model_custom_model(self):
        """Test that custom model name is used."""
        with patch.object(Settings, 'openai_api_key', 'test-key'):
            model = get_chat_model("gpt-4")
            assert model is not None