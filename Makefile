create_tables:
	python -m scripts.create_tables

drop_tables:
	python -m scripts.drop_tables

populate_tables:
	python -m scripts.populate_tables

run:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000