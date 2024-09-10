PYTHON=python
PIP=pip
BACKEND_DIR=backend/
FRONTEND_DIR=frontend/ticket_booking/
DJANGO_MANAGE=manage.py
DB_NAME=ticket_booking
DB_USER=postgres

backend-setup: ## Install backend dependencies
	$(PIP) install -r requirements.txt

frontend-setup: ## Install frontend dependencies
	cd $(FRONTEND_DIR) && npm install

database-setup: ## Create postgreSQL database and migrate tables
	echo "Create a database named $(DB_NAME) for user $(DB_USER)"
	psql -U $(DB_USER) -c "CREATE DATABASE $(DB_NAME);" || echo "Database $(DB_NAME) already exists"
	$(MAKE) migrate

setup: backend-setup frontend-setup database-setup ##Setup backend, frontend and database

run-backend: ## Run backend server
	cd $(BACKEND_DIR) && $(PYTHON) $(DJANGO_MANAGE) runserver

run-frontend: ## Run frontend server
	cd $(FRONTEND_DIR) && npm run serve

migrate: ## Make Django migrations
	cd $(BACKEND_DIR) && $(PYTHON) $(DJANGO_MANAGE) migrate

update: ## Install missing backend dependencies after project changes
	pip install -U -r requirements.pip