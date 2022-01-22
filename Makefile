install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run --username ' ' --password ' '

package-install:
	python3 -m pip install --user dist/*.whl

patch:
	poetry install
	poetry version patch
	poetry build
	poetry publish --dry-run --username ' ' --password ' '

lint:
	poetry run flake8 brain_games

.PHONY: install test lint selfcheck check build
