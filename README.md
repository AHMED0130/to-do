# to-do
### RUN docker build -t todo-app /path 
----------------------------------
docker-compose up
docker exec -it todo-app bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
