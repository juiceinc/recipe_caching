.PHONY: all docs tests precommit release .FORCE

all: docs flake8 tests

docs:
	cd docs && make html

autodocs:
	sphinx-autobuild docs docs/_build/html/ --port 8001

tests:
	py.test --cov-config .coveragerc --cov=recipe tests/

precommit:
	pre-commit run --all-files

flake8:
	flake8 . --exit-zero --max-complexity 12 --exclude=__init__.py

releease:
	rm -f dist/*
	python setup.py bdist_wheel sdist
	twine upload -r pypi dist/

