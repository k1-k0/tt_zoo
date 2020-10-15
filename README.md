## Usage
##### Define envs
##### Setup and launch
For building Docker images you need to execute following command
```
docker build -t tt_zoo:1.0 .
```
After that execute commands for database migration and creating Django superuser:
```
docker run -d -p 8000:8000 --name ztt tt_zoo:1.0
docker exec ztt python manage.py makemigrations
docker exec ztt python manage.py migrate
docker exec ztt python manage.py createsuperuser
```

Go to **http://localhost:8000**