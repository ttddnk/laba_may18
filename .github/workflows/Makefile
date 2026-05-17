setup:
	pip install ruff pytest

lint:
	ruff check .

test:
	pytest test_func.py -v

build:
	python setup.py sdist

all: setup lint test build
