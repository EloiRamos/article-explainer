<div align="center">

# Article Explainer

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6.7-green?logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![LangGraph Swarm](https://img.shields.io/badge/LangGraph%20Swarm-0.0.14-orange?logo=langchain&logoColor=white)](https://github.com/langchain-ai/langgraph-swarm)
[![Ollama](https://img.shields.io/badge/Ollama-Ready-purple?logo=ollama&logoColor=white)](https://ollama.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AI-Powered Document Analysis with Multi-Agent Intelligence**

An intelligent document analysis tool that transforms complex technical articles into easily understandable explanations using a team of specialized AI agents. Built with LangGraph Swarm Architecture, this application demonstrates how multiple AI agents can collaborate to provide comprehensive document analysis, analogies, summaries, and technical breakdowns.

[Quick Start](#quick-start) • [Features](#features) • [Usage](#usage) • [Development](#development)

</div>

---

## What Makes This Special

**Multi-Agent Intelligence**: Instead of a single AI model, this application uses a team of specialized agents that collaborate to provide nuanced, comprehensive explanations.

**Local & Cloud Ready**: Works with both OpenAI's powerful models and local Ollama instances for maximum flexibility and privacy.

**Interactive PDF Analysis**: Upload any PDF and engage in a conversation about its content with AI agents that understand context and can provide explanations at multiple levels.

## Application Screenshots

### Usage Explanation and Interface
![Usage Explanation and Interface](data/screenshots/img.png)

### Article Explainer Main Interface
![Article Explainer Main Interface](data/screenshots/main_interface.png)

## Features

<div align="center">

|     Core Functionality      |      AI Agents       | Technical                    |
| :-------------------------: | :------------------: |
|   PDF Upload & Processing   |   Summarizer Agent   | Real-time Processing         |
| Interactive Chat Interface  |   Explainer Agent    | LangGraph Swarm Architecture |
|    Integrated PDF Viewer    |   Analogy Creator    | Privacy-First Design         |
|  Multi-turn Conversations   |   Developer Agent    | Web-based Interface          |
| Document Structure Analysis | Vulnerability Expert | Docker Support               |

</div>

### Key Capabilities

- **Document Understanding**: Upload PDFs and ask questions about their content
- **Multi-Expert Analysis**: Five specialized AI agents collaborate to provide comprehensive explanations
- **Agent Handoffs**: Agents intelligently transfer control to provide the best expertise for each query
- **Context Preservation**: Maintains document context throughout conversations
- **Fast Processing**: Optimized for quick document analysis and response generation
- **Privacy Focused**: Option to run entirely locally with Ollama

## Quick Start

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/) (for local AI) or OpenAI API key
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/EloiRamos/article-explainer.git
   cd article-explainer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```

   Edit `.env` with your configuration:
   ```bash
   # For OpenAI (recommended for best results)
   OPENAI_API_KEY="your-openai-api-key-here"

   # OR for local Ollama (privacy-first)
   # OLLAMA_BASE_URL="http://localhost:11434"
   # OLLAMA_MODEL="qwen3:4b"
   ```

4. **Start Ollama (if using local AI)**
   ```bash
   ollama pull qwen3:4b
   ollama serve
   ```

5. **Launch the application**
   ```bash
   streamlit run article_explainer_page.py
   ```

6. **Open your browser** and navigate to `http://localhost:8501`

## Usage

### Basic Workflow

1. **Upload a PDF** using the sidebar file uploader
2. **Wait for processing** - the AI will analyze the document structure and content
3. **Start chatting** - ask questions about the document content
4. **Get expert responses** - the agent team will provide detailed explanations, summaries, analogies, or technical breakdowns

### Example Queries

Try asking the Article Explainer:

- *"Summarize this document in 3 bullet points"*
- *"Explain the most complex concepts using simple analogies"*
- *"What are the key technical innovations described here?"*
- *"Give me a TL;DR with the main arguments"*
- *"Are there any security considerations mentioned?"*
- *"Provide code examples for the concepts discussed"*

## Architecture

The Article Explainer uses a sophisticated multi-agent architecture built on LangGraph Swarm:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   PDF Upload    │───▶│  Content Loader  │───▶│   Document      │
│   & Processing  │    │  & Text Extract │    │   Processing    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                        │
┌───────────────────────────────────────┼────────────────────────────────────────────────────────┐
│                                                      │                                                        │
│                    ┌─────────────────┐               │               ┌─────────────────┐                    │
│                    │   LangGraph     │               │               │   Streamlit     │                    │
│                    │     Swarm       │◀──────────────┘               │   Web Interface │                    │
│                    │  Architecture   │                                └─────────┘                    │
│                    └─────────────────┘                                                        │
│                              │                                                                │
│                    ┌─────────────────┐               ┌─────────────────┐                    │
│                    │   Summarizer    │               │   Developer     │                    │
│                    │     Agent       │               │     Agent       │                    │
│                    └─────────────────┘               └─────────────────┘                    │
│                              │                                                                │
│                    ┌─────────────────┐               ┌─────────────────┐                    │
│                    │   Explainer     │               │ Vulnerability   │                    │
│                    │     Agent       │               │    Expert       │                    │
│                    └─────────────────┘               └─────────────────┘                    │
│                              │                                                                │
│                    ┌─────────────────┐                                                        │
│                    │ Analogy Creator │                                                        │
│                    │     Agent       │                                                        │
│                    └─────────────────┘                                                        │
└────────────────────────────────┘
```

### Agent Roles

- **Summarizer**: Provides concise summaries and key points
- **Explainer**: Breaks down complex concepts step-by-step
- **Analogy Creator**: Creates relatable analogies and metaphors
- **Developer**: Provides code examples and technical implementations
- **Vulnerability Expert**: Analyzes potential weaknesses and security considerations

## Development

### Project Structure

```
article-explainer/
├── config/              # Configuration management
│   ├── settings.py      # Pydantic settings with validation
│   └── __init__.py
├── data/                # Project data and assets
│   ├── sample_pdfs/     # Example PDF documents
│   └── screenshots/     # Application screenshots
├── docs/                # Documentation
├── explainer/           # Core AI agent logic
│   ├── service/         # Utilities and services
│   ├── graph.py         # Multi-agent orchestration
│   └── prompts.py       # Agent system prompts
├── logs/                # Application logs
├── tests/               # Unit and integration tests
├── article_explainer_page.py # Main Streamlit application
├── pyproject.toml       # Project configuration
├── .env.example         # Environment template
├── logging.conf         # Logging configuration
└── README.md           # This file
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=explainer --cov-report=html

# Run specific tests
pytest tests/test_config.py
```

### Code Quality

```bash
# Format code
black .

# Lint code
ruff check .

# Type checking
mypy .

# Pre-commit hooks
pre-commit run --all-files
```

## Performance & Compatibility

### Supported File Types
- PDF documents (primary support)
- Text extraction from complex layouts
- Multi-page document processing

### AI Model Options

| Provider   | Model       | Setup         | Privacy | Speed | Cost        |
| ---------- | ----------- | ------------- | ------- | ----- | ----------- |
| **OpenAI** | GPT-4o-mini | API Key       | Cloud   | Fast  | Pay-per-use |
| **Ollama** | Qwen3:4b    | Local Install | Private | Local | Free        |

### System Requirements

- **Minimum**: Python 3.9+, 4GB RAM, 2GB storage
- **Recommended**: Python 3.11+, 8GB RAM, 5GB storage, GPU (for Ollama)

## Contributing

We welcome contributions! Here's how you can help:

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Ensure all tests pass: `pytest`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

### Contribution Ideas

- [ ] Add support for more document formats (DOCX, TXT, etc.)
- [ ] Implement document comparison features
- [ ] Add export functionality (PDF reports, summaries)
- [ ] Create a mobile-responsive interface
- [ ] Add support for multiple languages
- [ ] Implement document versioning and history

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **LangChain** for the powerful LangGraph and Swarm architectures
- **Streamlit** for the amazing web interface framework
- **Ollama** for making local AI accessible
- **OpenAI** for advancing AI capabilities

---

<div align="center">

**Made with love by AI enthusiasts**

[Star this repo](https://github.com/EloiRamos/article-explainer) | [Report Issues](https://github.com/EloiRamos/article-explainer/issues) | [Discussions](https://github.com/EloiRamos/article-explainer/discussions)

</div>
