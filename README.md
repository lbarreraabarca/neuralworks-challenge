# NeuralWorks Challenge

This microservice has an architecture oriented to events. Also, it's an endpoint developed in Python using Flask libraries and a Postgres connector. As well, this endpoint used some components of port and adapters patterns desing.

## Pre requisites

- You must installed Docker 20 or later.
- You need to have installed Python 3.7 or later.

## Getting started
### Preprocessing 
I've developed a simple component for processing `trips.csv` file. The target was could transforming csv file to `INSERT` SQL statements. This one I make in [data/getSQLStatement.py](https://github.com/lbarreraabarca/neuralworks-challenge/blob/main/data/getSQLStatement.py) pipeline. If you want to run this pipeline using the following command:

```bash
python data/getSQLStatement.py
```

### Prepare environment
You need to create a database. Therefore, we'll docker for create a container that has a Postgres database. It's therefore you must run te following command [database/run.sh](https://github.com/lbarreraabarca/neuralworks-challenge/blob/main/database/run.sh):

```bash
bash database/run.sh
```

You can validate that database is working:
```bash
docker ps -a
```

## Run Application
For run the application you need to execute the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r src/requirements.txt
cd src
python App.py
```

## Inserting data through oriented to events architecture
For the question, *Automated process for ingest and store data on demand*. I've developed an endpoint that allows take a request and insert to database. 
The endpoint where you could insert events is [localhost:8080/api/v1/trip-event/insert](http://127.0.0.1:8080/api/v1/trip-event/insert). As well, the payload structure is:
```json
{
    "region": "Prague",
    "origin_coord": "POINT (14.56 50.65)",
    "destination_coord": "POINT (14.56 50.65)",
    "datetime": "2018-05-28 09:03:40",
    "datasource": "funny_car"
}
```

### Request
```bash
curl --location --request POST 'http://127.0.0.1:8080/api/v1/trip-event/insert' \
--header 'Content-Type: application/json' \
--data-raw '{
    "region": "Prague",
    "origin_coord": "POINT (14.4973794438195 50.00136875782316)",
    "destination_coord": "POINT (14.43109483523328 50.04052930943246)",
    "datetime": "2018-05-28 09:03:40",
    "datasource": "funny_car"
}'
```

You should receive a response something like that:
```json
{
    "response": "Payload stored successfully into database."
}
```

## Weekly average of trip by region
For the question, *A service allows returns the weekly average for a bounding box and the region*. I've developed an endpoint that allows take a request and make a query over database. The endpoint where you could apply the query is [localhost:8080/api/v1/trip-event/trip-per-week](http://127.0.0.1:8080/api/v1/trip-event/trip-per-week). Also, the payload structure is:

```json
{
    "coordinate": "origin_coord",
    "lower_coord": "POINT (-180 -90)",
    "upper_coord": "POINT (180 90)"
}
```
### Constraint
- `coordinate` field just could have these values `origin_coord` and `destination_coord`. In other case the request wouldn't be processed.

### Request
```bash
curl --location --request POST 'http://127.0.0.1:8080/api/v1/trip-event/trip-per-week' \
--header 'Content-Type: application/json' \
--data-raw '{
    "coordinate": "origin_coord",
    "lower_coord": "POINT (-180 -90)",
    "upper_coord": "POINT (180 90)"
}'
```
You should receive a response something like that:

```json
{
    "response": [
        {
            "region": "Hamburg",
            "trip_amount_per_week": "5.6000000000000000"
        },
        {
            "region": "Prague",
            "trip_amount_per_week": "6.8000000000000000"
        },
        {
            "region": "Turin",
            "trip_amount_per_week": "7.6000000000000000"
        }
    ]
}
```

## Scalability and Cloud environment

For solution be scalable I'll let avalaible a cloud solution. For the on demand ingest events I'll use a Pub/Sub products. A topic where you should send the event. Then, this topic will be connected to Pub/Sub Subscription. This subscription  will be push type and will delivered the events to Cloud Run endpoint. This endpoint should store the data into CloudSQL database. Also, the endpoint may receive request from Internet through token bearer authentification. 

![High level design](https://raw.githubusercontent.com/lbarreraabarca/neuralworks-challenge/main/images/high-level-design.png)

