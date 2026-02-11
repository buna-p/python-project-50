build:
	uv build

install:
	uv sync

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check gendiff

tests:
	uv run ruff check gendiff
	uv run pytest -xvv

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml