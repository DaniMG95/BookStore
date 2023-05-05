

## Deploy dockers

```
docker build . -t bookapi
docker run --name bookstore-mysql --net book-net -v C:\Users\dani_\Documents\db:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=12345 -e MYSQL_DATABASE=db -p 3306:3306 -d mysql
docker run -d --name bookapi --net book-net -p 80:80 bookapi
```


## Deploy dockers compose

```
docker compose up
```


# Pre-commit

```
pre-commit install  
pre-commit install --hook-type prepare-commit-msg
```
