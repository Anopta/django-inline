.PHONY: setup migrate

setup:
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py makemigrations artist
	python manage.py migrate

migrate:
	python manage.py makemigrations artist
	python manage.py migrate
