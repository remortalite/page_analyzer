lint:
	poetry run flake8 .


run:
	poetry run flask --app page_analyzer/app.py --debug run
