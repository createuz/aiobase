
project_dir := .
package_dir := app

.PHONY: help
help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Formatting & Linting

.PHONY: reformat
reformat: ## Reformat code
	@python3 ruff format $(project_dir)
	@python3 ruff check $(project_dir) --fix

.PHONY: lint
lint: reformat ## Lint code
	@python3 mypy $(project_dir)

VENV ?= ./venv
ALEMBIC := $(VENV)/bin/alembic
PY := $(VENV)/bin/python

.PHONY: migration
migration: ## Make database migration
	@$(ALEMBIC) revision \
	  --autogenerate \
	  --rev-id $(shell $(PY) alembic/_get_revision_id.py) \
	  --message $(message)

.PHONY: migrate
migrate: ## Apply database migrations
	@$(ALEMBIC) upgrade head

##@ App commands
.PHONY: run
run: ## Run bot
	@python3 python -O -m $(package_dir)

##@ Other
.PHONY: name
name: ## Get top-level package name
	@echo $(package_dir)
