import datacompy
import pandas as pd
from pathlib import Path

class Compare:

    def data_comapre(self, df1):
            file_path = Path('Data/100_Records.csv')
            df2 = pd.read_csv(file_path)

            compare = datacompy.Compare(
                df1,
                df2,
                join_columns='EMP ID',  #You can also specify a list of columns eg ['policyID','statecode']
                abs_tol=0, #Optional, defaults to 0
                rel_tol=0, #Optional, defaults to 0
                df1_name='DB_Values', #Optional, defaults to 'df1'
                df2_name='Source_Values' #Optional, defaults to 'df2'
            )
            print (compare.report())