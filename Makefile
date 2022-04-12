PYTHON = python3

restart:
	@echo "Reiniciando projeto..."
	docker-compose down -v
	@echo "Removendo migrações antigas..."
	@sudo rm -rf src/roit-api/migrations
	@echo "Reconstruindo a aplicação..."
	docker-compose up -d --build
	docker-compose exec web aerich init -t app.db.TORTOISE_ORM
	docker-compose exec web aerich init-db
	@echo "Host de acesso para o banco de dados!"
	@docker inspect roit-challenger_web-db_1 | grep -i IPAddress | grep 1
	cd src/roit-api/; . env-api/bin/activate; \
				${PYTHON} scripts/upload_tables.py; \
				deactivate
	@echo "Projeto reiniciado!"

run:
	@echo "Inicializando projeto..."
	docker-compose build
	docker-compose up -d
	python src/roit-api/scripts/upload_tables.py
	@echo "Projeto iniciado!"


clear:
	docker rmi $(docker images -f "dangling=true" -q) 
