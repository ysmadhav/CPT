import pandas as pd

class FileOps:

    def red_file_based_on_delimiter(self, file_path, file_delimiter):
        df = pd.read_csv(file_path, sep=file_delimiter)
        return df


