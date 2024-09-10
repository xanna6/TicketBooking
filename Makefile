PYTHON=python
PIP=pip
BACKEND_DIR=backend/
FRONTEND_DIR=frontend/ticket_booking/
DJANGO_MANAGE=manage.py
DB_NAME=ticket_booking
DB_USER=postgres

backend-setup: ## Install backend dependencies
	@$(PIP) install -r requirements.txt

frontend-setup: ## Install frontend dependencies
	@cd $(FRONTEND_DIR) && npm install

database-setup: ## Create postgreSQL database and migrate tables
	@echo "Create a database named $(DB_NAME) for user $(DB_USER)"
	@psql -U $(DB_USER) -c "CREATE DATABASE $(DB_NAME);" 2>/dev/null
	@if psql -U $(DB_USER) -lqt | cut -d \| -f 1 | grep -qw $(DB_NAME); then
		$(MAKE) migrate
	else
		@echo "Failed to create database, skipping migrations"
	fi

setup: backend-setup frontend-setup database-setup ##Setup backend, frontend and database

run-backend: ## Run backend server
	@cd $(BACKEND_DIR) && $(PYTHON) $(DJANGO_MANAGE) runserver

run-frontend: ## Run frontend server
	@cd $(FRONTEND_DIR) && npm run serve

migrate: ## Make Django migrations
	@cd $(BACKEND_DIR) && $(PYTHON) $(DJANGO_MANAGE) migrate

update: ## Install missing backend dependencies after project changes
	@pip install -U -r requirements.pip

help:
	awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)