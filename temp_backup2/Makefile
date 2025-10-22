.PHONY: help install dev-install test test-cov lint format type-check pre-commit clean docker-build docker-run

# Default target
help:
	@echo "Available commands:"
	@echo "  install      - Install production dependencies"
	@echo "  dev-install  - Install development dependencies"
	@echo "  test         - Run tests"
	@echo "  test-cov     - Run tests with coverage"
	@echo "  lint         - Run linting tools (ruff, black, mypy)"
	@echo "  format       - Format code with black and isort"
	@echo "  pre-commit   - Run pre-commit hooks"
	@echo "  clean        - Clean build artifacts and cache"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run   - Run Docker container"

# Installation
install:
	uv sync --no-dev

dev-install:
	uv sync

# Testing
test:
	uv run pytest

test-cov:
	uv run pytest --cov=src --cov-report=html --cov-report=term-missing

# Code quality
lint:
	uv run ruff check .
	uv run black --check .
	uv run mypy .

format:
	uv run black .
	uv run isort .

type-check:
	uv run mypy .

# Pre-commit
pre-commit:
	uv run pre-commit run --all-files

# Cleanup
clean:
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

# Docker
docker-build:
	docker build -t article_explainer .

docker-run:
	docker run -p 8501:8501 --env-file .env article_explainer