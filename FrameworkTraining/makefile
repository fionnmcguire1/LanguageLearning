
build:
	docker-compose build --no-cache

run:
	docker-compose up -d
	docker-compose run server bash -c "python manage.py migrate"
	docker-compose run server bash -c "python manage.py runserver 0.0.0.0:5000"

enter:
	docker exec -it frameworktraining_server_1 bash

test:
	docker-compose run server bash -c "pytest"
