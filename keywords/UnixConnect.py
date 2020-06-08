from typing import Any

import paramiko
from robot.api import logger
from robot.api.deco import keyword


class UnixConnect:

    def __init__(self):
        self.hostname = '192.168.0.15'
        self.port = 22
        self.username = 'root'
        self.password = 'root'

    @keyword
    def get_unix_connection(self, unix_hostname: str, unix_username: str, unix_password: str) -> Any:
        try:
            ssh_client_connection = paramiko.SSHClient()
            ssh_client_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # ssh_client_connection.connect(hostname=self.hostname, username=self.username, password=self.password)
            ssh_client_connection.connect(hostname=unix_hostname, username=unix_username, password=unix_password)
            return ssh_client_connection
        except paramiko.BadHostKeyException as err:
            logger.error('Could not verify hostkey for server: %s. Error: %s', self.hostname, str(err))
        except paramiko.AuthenticationException as err:
            logger.error('Could not authenticate on server: %s. Error: %s', self.hostname, str(err))
        except paramiko.SSHException as err:
            logger.error('Could not create SSH connection on server %s. Error: %s',
                         self.hostname, str(err))

    @keyword
    def get_remote_source_file(self, ssh_client_connection: Any, remote_file_path: str, local_file_path: str):
        ftp_client = ssh_client_connection.open_sftp()
        ftp_client.get(remote_file_path, local_file_path)
        ftp_client.close()
