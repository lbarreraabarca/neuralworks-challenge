import psycopg2

class PostgreSQLOperator(object):
    def __init__(self,
                 host: str,
                 port: int,
                 databaseName: str,
                 username: str,
                 password: str):
        self._host = host
        self._port = port
        self._databaseName = databaseName
        self._username = username
        self._password = password

    def getConnection(self):
        try:
            return psycopg2.connect(host=self.host,
                                    port=self.port,
                                    database=self.databaseName,
                                    user=self.username,
                                    password=self.password)
        except Exception:
            raise Exception(f'Cannot not connect to {self.host}')

    def insert(self, statement: str):
        try:
            connection = self.getConnection()
            cursor = connection.cursor()
            cursor.execute(statement)
            connection.commit()
            cursor.close()
        except Exception:
            raise Exception(f'Error while it was inserting data. Statement {statement}')

    def query(self, statement: str):
        try:
            connection = self.getConnection()
            cursor = connection.cursor()
            cursor.execute(statement)
            result = cursor.fetchall()
            columns = list(cursor.description)
            output = []
            for row in result:
                columnCount = 0
                rowDict = {}
                for column in columns:
                    rowDict[column.name] = row[columnCount]
                    columnCount += 1
                output.append(rowDict)
            cursor.close()
            return output
        except Exception:
            raise Exception(f'Error while it was inserting data. Statement {statement}')

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def databaseName(self):
        return self._databaseName

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
