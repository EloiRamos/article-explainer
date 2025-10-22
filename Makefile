install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

run:
	python -m streamlit run article_explainer_page.py
run-dev:
	python -m streamlit run article_explainer_page.py --server.runOnSave true

format:
	black .
	isort .

lint:
	ruff check .

fix:
	ruff check --fix .

check:
	black --check .
	ruff check .

mypy:
	mypy .

test:
	pytest

test-cov:
	pytest --cov=src --cov-report=html

.PHONY: install install-dev run run-dev format lint fix check mypy test test-cov