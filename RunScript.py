from keywords.UnixConnect import UnixConnect
from keywords.FileOps import FileOps
from keywords.DBOps import DBOps
from keywords.Compare import Compare
from keywords.ReadConfig import ReadConfig
import os


# # ****************** Get SSH Connection and get remote file **********************
#
# ssh_connection = UnixConnect()
# ssh_connect = ssh_connection.get_unix_connection()
#
# remotepath = '/root/files/Tab_FlyRNAi_data_baseline_vs_EGF.txt'
# localpath = 'Data/Source_Files/Tab_FlyRNAi_data_baseline_vs_EGF.txt'
# ssh_connection.get_remote_source_file(ssh_connect, remotepath, localpath)
#
# remotepath = '/root/files/Pipe_PowerReactorStatusForLast365Days.txt'
# localpath = 'Data/Source_Files/Pipe_PowerReactorStatusForLast365Days.txt'
# ssh_connection.get_remote_source_file(ssh_connect, remotepath, localpath)
#
#
#
# # ******************* Read the file based onDelimiter ************************
#
# read_file = FileOps()
# df = read_file.red_file_based_on_delimiter(file_path='Data/Source_Files/Tab_FlyRNAi_data_baseline_vs_EGF.txt', file_delimiter='\t')
# print (df)
#
#
# df = read_file.red_file_based_on_delimiter(file_path='Data/Source_Files/Pipe_PowerReactorStatusForLast365Days.txt', file_delimiter='|')
# print (df)
#
#
#
# # ************ Get DB Connection and Execute Query ******************
#
# db_ops = DBOps()
# db_connection = db_ops.get_db_connection()
# db_data = db_ops.execute_query(db_connection, query='select * from CPTDEMO.Employee')
# print(db_data)
#
#
# # ************ Compare Results using DataCompy ******************
#
# validate_data =  Compare()
# validate_data.data_comapre(db_data)


#************* Get Config Values **********************************

config_value = ReadConfig()
value = config_value.get_config_details('dev', 'teradata_host')
print (value)
db_password = os.environ.get("teradata_password")
print(db_password)