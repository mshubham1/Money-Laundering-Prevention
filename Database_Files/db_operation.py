from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from app_logger.logger import App_Logger
import pandas as pd

class Connector:
    def __init__(self):
        """
        :DESC: Creates connection with Database when backend thread runs.
        """
        self.logger = App_Logger()
        file = open("log_file/Db_Operation.txt", 'a+')
        self.logger.log(file, "Start of Training !!" )
        file.close()
        self.Client_id = 'wSWyifYUiwzIMBZgsIQwSCYf'
        self.Client_secret = 'DzvFe2GpiIM0zeTCjkfi7mafa,5Uzct823_E7.RPo2byOWXlqD_ZDKt9a187TDZ-Z7TylJZqG3Q09Hd.5eMm2BbRHipZBHosQg,T7wJTQHlxaN0Y76_aLpFf.EMo6XKd'

        cloud_config = {'secure_connect_bundle': 'secure-connect-money-laundering.zip'}
        auth_provider = PlainTextAuthProvider(self.Client_id, self.Client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        

        try:
            
            self.session = cluster.connect('mykeyspace')
            #self.session.execute("CREATE KEYSPACE laundering WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 2}")
            file = open("log_file/Db_Operation.txt", 'a+')
            self.logger.log(file, "Opened Money Laundering Prevention database successfully!" )
            file.close()
        except ConnectionError:
            file = open("log_file/Db_Operation.txt", 'a+')
            self.logger.log(file, "Error while connecting to database: %s" %ConnectionError)
            file.close()
            raise ConnectionError

    def create_table(self):
        """ Creates table if not existed into database"""
        try:
            self.session.execute("use mykeyspace")
            self.session.execute("select release_version from system.local")
            self.session.execute("CREATE TABLE IF NOT EXISTS user_data (id uuid PRIMARY KEY,step int,amount int,oldbalanceOrg int,oldbalanceDest int,trans_type text);")
            file = open("log_file/Db_Operation.txt", 'a+')
            self.logger.log(file, "Successfully created table user_data in database money_laundering_prevention!! Exited the create_table function.!")
            self.logger.log(file, "Exited the create_table method of the Connector Class!!")
            file.close()
           
        except Exception as e:
            file = open("log_file/Db_Operation.txt", 'a+')
            self.logger.log(file, "Error while creating table: %s " % e)
            file.close()
            raise e

    def addData(self, result):
        """
        :param result: Gets data from user and puts it into database
        :return:
        """
        file = open("log_file/Db_Operation.txt", 'a+')
        self.logger.log(file, "Inside addData ! Adding Data to user_data table in database.!!")
        file.close()

        try:
            column = "id, step, amount,oldbalanceOrg, oldbalanceDest , trans_type"
            value = "{0},{1},{2},{3},{4},'{5}'".format('uuid()', 
                                                                    result['step'], result['amount'],
                                                                    result['oldbalanceOrg'], result['oldbalanceDest'],
                                                                    result['trans_type']) 
            file = open("log_file/Db_Operation.txt", 'a+')
            self.logger.log(file, "String Created!")
            custom = "INSERT INTO user_data({}) VALUES({});".format(column, value)
            #custom = "INSERT INTO user_data (id, step, amount, oldbalanceOrg, oldbalanceDest , trans_type) VALUES (uuid(), result['step'], result['amount'],result['oldbalanceOrg'], result['oldbalanceDest'], result['trans_type']);"
            #self.session.execute("INSERT INTO user_data (id, step, amount, oldbalanceOrg, oldbalanceDest, trans_type) VALUES (201, 1, 16000, 15400, 5410, 'CASH_OUT')")                                            
            self.logger.log(file, "Key Created!!")
            self.session.execute("USE mykeyspace")
            
            output = self.session.execute(custom)
            #output = self.session.execute( "INSERT INTO user_data (id, step, amount, oldbalanceOrg, oldbalanceDest , trans_type)"
            #"VALUES (uuid(), result['step'], result['amount'],result['oldbalanceOrg'], result['oldbalanceDest'], result['trans_type'])")
            self.logger.log(file, "Data inserted {}".format(output))
            self.logger.log(file, "Exited the addData method of the Connector Class!!")
            file.close()

        except Exception as e:
            file = open("log_file/Db_Operation.txt", 'a+')
            self.logger.log(file, "Error while adding data to  table!!" )
            file.close()
            raise e

    def getData(self):
        """
        :DESC: Retrieves Data from Database
        """
        try:
            
            self.session.execute("use mykeyspace")
            row = self.session.execute("SELECT * FROM user_data;")
            collection = []
            for i in row:
                collection.append(tuple(i))
            df=pd.DataFrame(collection,columns=['uuid','step', 'amount','oldbalanceOrg', 'oldbalanceDest' , 'trans_type'])
            df.to_csv("input_file.csv")
            file = open("log_file/Db_Operation.txt", 'a+')
            self.logger.log(file, "Data has been Fetch Successfully from the Table: user_data!!" )
            self.logger.log(file, "Exited the getData method of the Connector Class!!")
            file.close()
            return tuple(collection)
            
        except Exception as e:
            file = open("log_file/Db_Operation.txt", 'a+')
            self.logger.log(file, "Error while fetching data from the   table!!" )
            file.close()
            raise e