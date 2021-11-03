from sklearn.model_selection import train_test_split
from Database_Files.db_operation import Connector
from app_logger.logger import App_Logger
from src.data_preprocessing import Preprocessor
from src import tuner
import numpy as np
import pandas as pd
import pickle 


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
            # export data in table to csvfile
            #getting the dat
            """
            self.logger.log(self.file_object, "Getting the data from input file for Preprocessing!!")
            df=pd.read_csv("training_files/dataset.csv")


            preprocessor = Preprocessor(self.file_object,self.logger)
            df=preprocessor.remove_columns(df,['isFlaggedFraud','nameOrig','nameDest']) # remove the column as it doesn't contribute to prediction.
            
            #check if null present in the columns or not
            is_null_present,cols_with_missing_values=preprocessor.is_null_present(df)
            
            #if null present impute the misssing values
            if(is_null_present):
                    data=preprocessor.impute_missing_values(df,cols_with_missing_values)
            #data=preprocessor.remove_unwanted_spaces(self.data) # remove unwanted spaces from the dataframe
           # data.replace('?',np.NaN,inplace=True) # replacing '?' with NaN values for imputation
            
            # create separate features and labels
            X,Y=preprocessor.separate_label_feature(df,label_column_name='isFraud')

            # handling outliers on numerical feature
            numerical_feature=[feature for feature in X.columns if df[feature].dtypes=='float64']
            data_clean = preprocessor.handling_outliers(X,numerical_feature)

            #onehot encoding for categorical feature
            data_cat=preprocessor.one_hot_encoding(X)

            #concatinating the data_clean and data_cat 
            X_=pd.concat([data_clean,data_cat],axis=1)

         
            X,Y = preprocessor.handle_imbalanced_dataset(X_,Y)

            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

            model_finder=tuner.Model_Finder(self.file_object,self.logger) # object initialization

            #getting the best model for each of the clusters
            best_model_name,best_model=model_finder.get_best_model(X_train,y_train,X_test,y_test)

            #saving the best model to the directory.
            pickle.dump(best_model,"models/"+best_model_name+".pkl")


            # logging the successful Training
            self.logger.log(self.file_object, 'Successful End of Training')
            self.file_object.close()
            x=pd.DataFrame([[data]])
            output = best_model.predict(x)
            return output   """

        except Exception as e:
            # logging the unsuccessful Training
            self.logger.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception