GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)
PYTHON = python3
TARGET_MAX_CHAR_NUM=20

default: help

## Show this help message.
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

## Build application docker-compose.
build: 
	@docker-compose build
	@docker-compose up -d
	@docker-compose exec web aerich init -t app.db.TORTOISE_ORM
	@docker-compose exec web aerich init-db
	@docker inspect roit-challenger_web-db_1 | grep -i IPAddress | grep 1
	cd roit-api/; . env-api/bin/activate; \
				${PYTHON} scripts/upload_tables.py; \
				deactivate
	@docker-compose run -d minio mc policy set public minio/roit

## Remove dependencies created when running the application.
clear:
	@sudo rm -rf roit-api/migrations
	@sudo rm -rf minio/data

## List containers.
list_containers:
	@docker ps -a -q

## Stop containers.
stop: list_containers
	@docker-compose list_containers

## Stops containers and removes containers, networks and volumes created by up.
down:
	@docker-compose down -v

