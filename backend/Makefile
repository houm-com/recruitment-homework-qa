.ONESHELL:
.DEFAULT_GOAL := help

SHELL := /bin/bash

DEV_COMPOSE := @docker-compose --env-file=.env --project-name visits-app-local -f .docker/docker-compose.dev.yml

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)


# Remove volumes, networks, images and containers
# WARNING: This cleans ALL volumes, networks and volumes not just for this specific project
clean:
	@yes | docker volume prune
	@yes | docker network prune
	@yes | docker image prune
	@docker container prune


# Stop and remove Docker containers not just stopping it
down: 
	$(DEV_COMPOSE) down --remove-orphans


# Build base Docker images, it installs the requirements into the image
build-service:
	$(DEV_COMPOSE) build --no-cache

# Rebuild databae with initial test data
build-clean-database: 
	$(DEV_COMPOSE) run --rm api sh -c 'python database/setup.py'

# Rebuild in case of changes in the Dockerfile or you want to install new requirements into the image
rebuild-service: down build-service


# Run the project and get into a terminal
run-terminal:
	$(DEV_COMPOSE) run --service-ports --rm api bash || true
	$(MAKE) stop


# Run the project and start the api server
run-service:
	$(DEV_COMPOSE) run --service-ports --rm -i api sh -c 'dev up' || true
	$(MAKE) stop

# Used to create a fresh project, it will build the service and create a clean database
clean-install:
	$(MAKE) build-service
	$(MAKE) build-clean-database

# Run tests
run-tests:
	$(DEV_COMPOSE) run --rm api sh -c 'pytest tests/'

#Stop Docker containers without removing them. Useful if up command is run in detached mode
stop:
	$(DEV_COMPOSE) stop

# Generate migrations e.g. make migrate msg='migration'
migrate:
	$(DEV_COMPOSE) run --rm api sh -c 'alembic revision --autogenerate -m "${msg}"'

apply-migrations:
	$(DEV_COMPOSE) run --rm api sh -c 'alembic upgrade head'
