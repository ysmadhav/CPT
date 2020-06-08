from pathlib import Path

import datacompy
import pandas as pd
from robot.api.deco import keyword


class Compare:

    @keyword
    def data_compare(self, df1):
        file_path = Path('Data/100_Records.csv')
        df2 = pd.read_csv(file_path)

        compare = datacompy.Compare(
            df1,
            df2,
            join_columns='EMP ID',  # You can also specify a list of columns eg ['policyID','statecode']
            abs_tol=0,  # Optional, defaults to 0
            rel_tol=0,  # Optional, defaults to 0
            df1_name='DB_Values',  # Optional, defaults to 'df1'
            df2_name='Source_Values'  # Optional, defaults to 'df2'
        )
        print(compare.report())

    @keyword
    def records_only_in_source(self, df1):
        file_path = Path('Data/100_Records.csv')
        df2 = pd.read_csv(file_path)

        compare = datacompy.Compare(
            df1,
            df2,
            join_columns='EMP ID',  # You can also specify a list of columns eg ['policyID','statecode']
            abs_tol=0,  # Optional, defaults to 0
            rel_tol=0,  # Optional, defaults to 0
            df1_name='DB_Values',  # Optional, defaults to 'df1'
            df2_name='Source_Values'  # Optional, defaults to 'df2'
        )
        print(compare.df1_unq_rows)
