# vestGO


## Creating the database
```sh
docker-compose up -d postgres
docker exec -it vestgo_postgres_1 psql -U postgres
```
```sql
CREATE DATABASE vestgo_local;
```

## apply migrations
```sh
python manage.py migrate
```


## seeding initial data 
```sh
python manage.py seed_data
```


Use \q to exit from psql shell
Maybe you need add 'sudo' before docker commands or remove super user permissions from docker command

