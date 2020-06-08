import teradatasql
from robot.api import logger
import pandas as pd

class DBOps:

    def get_db_connection(self):

        try:
            connection = teradatasql.connect(host='192.168.0.15', user='dbc', password='dbc')
            return connection
        except teradatasql.DatabaseError as db_error:
            logger.error('Could not establish connection with the database')


    def execute_query(self, db_connection, query):
        df = pd.read_sql(query, db_connection)
        return df