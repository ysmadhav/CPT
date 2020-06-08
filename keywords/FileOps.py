from pathlib import Path

import pandas as pd
from robot.api.deco import keyword


class FileOps:

    @keyword
    def red_file_based_on_delimiter(self, file_path: Path, file_delimiter: str) -> pd:
        df = pd.read_csv(file_path, sep=file_delimiter)
        return df
