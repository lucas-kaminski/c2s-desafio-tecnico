create-tables:
	python -m scripts.create_tables

drop-tables:
	python -m scripts.drop_tables

populate-tables:
	python -m scripts.populate_tables

run-server:
	poetry run uvicorn app.server:app --reload --host 0.0.0.0 --port 8000

run-cli:
	poetry run python -m app.cli