PYTHON = python3

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

clear:
	@sudo rm -rf roit-api/migrations
	@sudo rm -rf minio/data

list_containers:
	@docker ps -a -q

stop: list_containers
	@docker-compose list_containers

down:
	@docker-compose down -v

