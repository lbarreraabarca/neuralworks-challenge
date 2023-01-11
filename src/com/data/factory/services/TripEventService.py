from com.data.factory.adapters.PostgreSQLOperator import PostgreSQLOperator

class TripEventService(object):
    host: str = 'localhost'
    port: int = 5455
    databaseName: str = 'postgres'
    username: str = 'postgres'
    password: str = 'pgPW'

    def invoke(self):
        return ({"response":"hello world"}, 200)
    
    def insert(self, payload: dict):
        try:
            postgres = PostgreSQLOperator(self.host, self.port, self.databaseName, self.username, self.password)
            
            region = payload['region']
            originCoord = payload['origin_coord']
            destinationCoord = payload['destination_coord']
            datetime = payload['datetime']
            datasource = payload['datasource']
            
            insertStatement = f"INSERT INTO challenge.trip_event values ('{region}', '{originCoord}', '{destinationCoord}', '{datetime}', '{datasource}');"
            postgres.insert(insertStatement)
            return ({"response":"Payload stored successfully into database."}, 200)
        except Exception as e:
            return ({
                "response":f"Occured an error while it was storing data into database."
                }, 500)
    
    def getTripPerWeek(self, payload: dict):
        try:
            postgres = PostgreSQLOperator(self.host, self.port, self.databaseName, self.username, self.password)
            query = f"""
            with trip_per_week as (
                select region,  DATE_PART('week', datetime) as week_number, count(1) as trip_amount 
                from challenge.trip_event te 
                where {payload['coordinate']} between '{payload['lower_coord']}' and '{payload['upper_coord']}'
                group by 1, 2
            )
            select region, avg(trip_amount) as trip_amount_per_week
            from trip_per_week
            group by 1;
            """
            result = postgres.query(query)
            return ({"response":result}, 200)
        except Exception:
            return ({
                "response":f"Occured an error while it was applying query over database."
                }, 500)

