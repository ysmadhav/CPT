import paramiko
from robot.api import logger


class UnixConnect:

    def __init__(self):
        self.hostname = '192.168.0.15'
        self.port = 22
        self.username = 'root'
        self.password = 'root'


    def get_unix_connection(self):
        try:
            ssh_client_connection=paramiko.SSHClient()
            ssh_client_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client_connection.connect(hostname=self.hostname, username=self.username, password=self.password)
            return ssh_client_connection
        except paramiko.BadHostKeyException as err:
            logger.error('Could not verify hostkey for server: %s. Error: %s', self.hostname, str(err))
        except paramiko.AuthenticationException as err:
            logger.error('Could not authenticate on server: %s. Error: %s', self.hostname, str(err))
        except paramiko.SSHException as err:
            logger.error('Could not create SSH connection on server %s. Error: %s',
                         self.hostname, str(err))



    def get_remote_source_file(self, ssh_client_connection, remotefilepath, localfilepath):
        ftp_client=ssh_client_connection.open_sftp()
        ftp_client.get(remotefilepath , localfilepath)
        ftp_client.close()