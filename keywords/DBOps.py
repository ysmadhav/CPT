from typing import Any

import pandas as pd
import teradatasql
from robot.api import logger
from robot.api.deco import keyword


class DBOps:

    @keyword
    def get_db_connection(self, host_name: str, user_name: str, unix_password: str) -> Any:
        try:
            connection = teradatasql.connect(host=host_name, user=user_name, password=unix_password)
            return connection
        except teradatasql.DatabaseError as db_error:
            logger.error('Could not establish connection with the database' + str(db_error))

    @keyword
    def execute_query(self, db_connection: Any, query: str) -> pd:
        df = pd.read_sql(query, db_connection)
        return df
