
# ------------- Lint ---------------------------------------

.PHONY: pre-commit pre-commit-update lint test test-all

pre-commit: ## apply pre-commit to all files
	pre-commit run --all-files

pre-commit-update: ## update pre-commit
	pre-commit autoupdate

lint: ## check style with flake8
	flake8 covid19pyclient tests



# ------------- Clean Artifacts (bytecode) -----------

.PHONY: clean clean-pyc clean-test clean-build

clean: clean-pyc clean-test clean-build clean-coverage ## remove all build, test and Python artifacts

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +



# ------------  Help  --------------------------------------

.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
