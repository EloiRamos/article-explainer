from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    ""Application settings with validation."""

    # OpenAI Configuration
    openai_api_key: Optional[str] = None
    openai_model: str = "gpt-4o-mini"

    # Ollama Configuration
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen3:4b"

    # Streamlit Configuration
    streamlit_port: int = 8501
    streamlit_address: str = "0.0.0.0"
    streamlit_headless: bool = True

    # Application Configuration
    max_pdf_chunks: int = 10
    log_level: str = "INFO"
    log_file: str = "logs/app.log"

    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"


# Global settings instance
settings = Settings()