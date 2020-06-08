from pathlib import Path

import yaml
from robot.api.deco import keyword


class ReadConfig:

    @staticmethod
    def read_yaml_file(file_path: Path, env: str, key_name: str) -> str:
        with open(Path(file_path)) as f:
            docs = yaml.load_all(f, Loader=yaml.FullLoader)
            for doc in docs:
                for k, v in doc.items():
                    for key in v:
                        return v[env][key_name]

    @keyword
    def get_config_details(self, env: str, key: str) -> str:

        file_path = Path('config/env.yaml')
        value = ReadConfig.read_yaml_file(file_path, env, key_name=key)
        return value
