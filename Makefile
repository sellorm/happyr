MASTER_VERSION := $(shell grep '^version = .*$$' pyproject.toml | awk '{print $$3}')
all: README.md

README.md: README.bashdown 
	bashdown README.bashdown > README.md

build:
	-rm -r ./dist/*
	poetry build

tidy:
	black happyr/
	pylint happyr/
	mypy --strict happyr

test:
	python3 -m coverage run -m unittest
	python3 -m coverage report

version:
	sed -i "s/^__version__ = .*$$/__version__ = \"$(MASTER_VERSION)\"/g" happyr/version.py

publish:
	poetry publish

clean:
	-rm -rf dist
	-rm -rf venv
	-rm -rf happyr/__pycache__
