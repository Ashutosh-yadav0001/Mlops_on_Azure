install:
	pip install --upgrade pip &&\
		pip install -r requirement.txt

test:
	python -m pytest -vv test_hello.py

format:
	black *.py

pylint:
	pylint hello.py

lint:
    pylint --disable=R,C hello.py



all: install lint test
