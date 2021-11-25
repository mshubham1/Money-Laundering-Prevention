from sklearn.model_selection import train_test_split
from Database_Files.db_operation import Connector
from app_logger.logger import App_Logger


class trainModel:

    def __init__(self):
        self.logger = App_Logger()
        self.dBOperation = Connector()
        self.file_object = open("log_file/Model_Training.txt", 'a+')
    def trainingModel(self,data):
         
        # Logging the start of Training
        self.logger.log(self.file_object, 'Start of Training !!')
        self.data=data
        try:
            self.logger.log(self.file_object, "Creating Training_Database and tables to store data.!!!")
            
            """db_operation of Table Creation, Data Insertion, and Extracting CSV file from table"""
            self.dBOperation.create_table()
            self.logger.log(self.file_object, "Table creation Completed!!")
            self.logger.log(self.file_object, "Insertion of Data into Table started!!!!")
            self.dBOperation.addData(self.data)
            self.logger.log(self.file_object, "Extracting csv file from table")
            self.dBOperation.getData()
           
        except Exception as e:
            # logging the unsuccessful Training
            self.logger.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception
