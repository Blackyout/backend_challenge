build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

migrate:
	docker-compose exec web python manage.py migrate

superuser:
	docker-compose exec web python manage.py createsuperuser

test:
	docker-compose exec web python manage.py test

lint:
	# Aquí irían comandos como flake8 o black si se instalan
	echo "Linting..."