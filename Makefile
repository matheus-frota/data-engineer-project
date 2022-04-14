PYTHON = python3

restart:
	@echo "Reiniciando o projeto..."
	docker-compose down -v
	@echo "Removendo migrações da API..."
	@sudo rm -rf roit-api/migrations
	@echo "Apagando o volume do bucket"
	@sudo rm -rf minio/data
	@echo "Reconstruindo a aplicação..."
	docker-compose up -d --build
	docker-compose exec web aerich init -t app.db.TORTOISE_ORM
	docker-compose exec web aerich init-db
	@echo "Host de acesso para o banco de dados!"
	@docker inspect roit-challenger_web-db_1 | grep -i IPAddress | grep 1
	cd roit-api/; . env-api/bin/activate; \
				${PYTHON} scripts/upload_tables.py; \
				deactivate
	@echo "Criando o bucket para o projeto"
	@docker-compose run -d minio mc policy set public minio/roit
	@echo "Projeto reiniciado!"

run:
	@echo "Inicializando projeto..."
	docker-compose build
	docker-compose up -d
	python roit-api/scripts/upload_tables.py
	@echo "Projeto iniciado!"


clear:
	docker rmi $(docker images -f "dangling=true" -q) 
