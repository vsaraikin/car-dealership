# Web service for multiple car dealers, their suppliers, and their buyers

### Setting up on local machine

You can create either a python venv or docker container.

1. For running via python local venv: 
   1. `pipenv install -r requirements.txt`
   2. `python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000`
2. For running via docker container: `docker-compose up`