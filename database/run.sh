#!/bin/bash

docker run --name challenge-neuralworks-db -p 5455:5432 --net=bridge -e POSTGRES_PASSWORD=pgPW -d postgis/postgis
docker cp ./database/script.sql challenge-neuralworks-db:/tmp/script.sql
docker exec -u postgres challenge-neuralworks-db psql postgres postgres -f /tmp/script.sql