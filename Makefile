.PHONY: install test serve clean lint format

install:
	pip install -r requirements.txt

test:
	python -m pytest -v

serve:
	python -c "from module_04_web.project.app import create_app; create_app().run(debug=True, port=5000)"

lint:
	ruff check .

format:
	ruff format .

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
