#!/bin/bash

docker run --name challenge-neuralworks -p 5455:5432 -e POSTGRES_PASSWORD=pgPW -d postgis/postgis
docker cp ./database/script.sql challenge-neuralworks:/tmp/script.sql
docker exec -u postgres challenge-neuralworks psql postgres postgres -f /tmp/script.sql