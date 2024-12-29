# vestGO


## Creating the database
```sh
docker-compose up -d postgres
docker exec -it vestgo_postgres_1 psql -U postgres
```
```sql
CREATE DATABASE vestgo_local;
```

Use \q to exit from psql shell
Maybe you need add 'sudo' before docker commands or remove super user permissions from docker command

