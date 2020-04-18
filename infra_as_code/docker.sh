#! /bin/sh

docker -v
docker network create raddit-network
docker network ls
docker volume create mongo-data
docker volume ls | grep mongo-data

docker run --name mongo-database \
    --volume mongo-data:/data/db \
    --network raddit-network \
    --detach mongo:3.2