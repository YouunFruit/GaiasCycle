# Docker Setup
## MYSQL

This project requires a mysql database to run, you can set one up by
running the following commands on a terminal

- get the mysql image from the repository

```
docker pull mysql
```
- run the container and set the password to "secret"

```
docker run --name gaiascycle_db -e MYSQL_ROOT_PASSWORD=secret -d mysql:latest
```
- then from the container's terminal, create the following database

```
docker exec -it gaiascycle_db sh
```

- once inside the container, access mysql by running the following command and inputting "secret" as the password
```
mysql
```
- The last step will be to create the database
- In a query console run the following.

```
CREATE DATABASE gaiascycle;
```

##Kafka

This Project also requires a kafka image to be run. Kafka will produce the dummy data needed to test our product.

- Pull a kafka image on docker
```
docker pull kafka

```
- Create and run a container
```
docker run -d --name broker apache/kafka:latest
```
