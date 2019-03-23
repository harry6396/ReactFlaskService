import mysql.connector

def connectDB(configuration):

    return mysql.connector.connect(
        host=configuration.host,
        user=configuration.user,
        passwd=configuration.password,
        database=configuration.database
    )


## This class is used for the configuration of database
class Configuration:
    host=''
    user=''
    password=''
    database=''

    def __init__(self, host, user, password, database):
        self.host=host
        self.user = user
        self.password = password
        self.database = database


