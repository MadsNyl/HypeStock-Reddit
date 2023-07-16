install:
	pip install -r requirements.txt

pushshift:
	python pushshift.py ${args}

run:
	python main.py ${args}

check:
	flake8 --ignore=E501 --per-file-ignores="__init__.py:F401"

format:
	black .