import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from imblearn.under_sampling import RandomUnderSampler
from scipy import stats

class Preprocessor:
    """ This class shall  be used to clean and transform the data before training.  """

    def __init__(self, file_object, logger_object):
        self.classname = self.__class__.__name__
        self.file_object = file_object
        self.logger_object = logger_object

        self.logger_object.log(self.file_object,f'Enter the class:{self.classname}')


    def remove_columns(self,data,columns):
        """ This method removes the given columns from a pandas dataframe."""
        self.funcname=self.remove_columns.__name__
        self.logger_object.log(self.file_object, f'Entered the function: {self.funcname} of the class: {self.classname}')
        self.data=data
        self.columns=columns
        try:
            self.useful_data=self.data.drop(labels=self.columns, axis=1) # drop the labels specified in the columns
            self.logger_object.log(self.file_object, f'Dropped the columns: {columns}')
            self.logger_object.log(self.file_object, 'Column removal Successful.Exited the remove_columns method of the Preprocessor class')
            return self.useful_data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in remove_columns method of the Preprocessor class. Exception message:  '+str(e))
            raise Exception()

    def separate_label_feature(self, data, label_column_name):
        """ This method separates the features and a Label Coulmns. """
        self.funcname=self.separate_label_feature.__name__
        self.logger_object.log(self.file_object, 'Entered the separate_label_feature method of the Preprocessor class')
        try:
            self.X=data.drop(labels=label_column_name,axis=1) # drop the columns specified and separate the feature columns
            self.Y=data[label_column_name] # Filter the Label columns
            self.logger_object.log(self.file_object,'Label Separation Successful. Exited the separate_label_feature method of the Preprocessor class')
            return self.X,self.Y
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in separate_label_feature method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object, 'Label Separation Unsuccessful. Exited the separate_label_feature method of the Preprocessor class')
            raise Exception()

    def is_null_present(self,data):
        """ This method checks whether there are null values present in the pandas Dataframe or not. """
        self.funcname=self.is_null_present.__name__
        self.logger_object.log(self.file_object, 'Entered the is_null_present method of the Preprocessor class')
        self.null_present = False
        self.cols_with_missing_values=[]
        self.cols = data.columns
        try:
            self.null_counts=data.isna().sum()
            for i in range(len(self.null_counts)):
                if (self.null_counts[i]>0):
                    self.null_present = True
                    self.missing_col.append(self.null_counts)
            self.logger_object.log(self.file_object, 'Checked  if the Null value present or not !')
            self.logger_object.log(self.file_object, f'Exited the function: {self.funcname} of the class: {self.classname}')
            return self.null_present,self.cols_with_missing_values
        except Exception as e:
            self.logger_object.log(self.file_object,f"Exception occured in {self.funcname} method of {self.classname} class. Exception message: {e}",)
            raise Exception()

    def impute_missing_values(self, data, cols_with_missing_values):
        """ This method replaces all the missing values in the Dataframe using KNN Imputer. """
        self.funcname=self.impute_missing_values.__name__
        self.logger_object.log(self.file_object, 'Entered the impute_missing_values method of the Preprocessor class')
        self.data= data
        self.cols_with_missing_values=cols_with_missing_values
        try:
            self.imputer = KNNImputer(n_neighbors=3, weights='uniform',missing_values=np.nan)
            for col in self.cols_with_missing_values:
                self.data[col] = self.imputer.fit_transform(self.data[col])
            self.logger_object.log(self.file_object, 'Imputing missing values Successful. Exited the impute_missing_values method of the Preprocessor class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in impute_missing_values method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object,'Imputing missing values failed. Exited the impute_missing_values method of the Preprocessor class')
            raise Exception()

    def handling_outliers(self,data,numerical_feature):
        self.funcname=self.handling_outliers.__name__
        self.data=data
        self.numerical_feature= numerical_feature
        self.logger_object.log(self.file_object,f'Entered the function: {self.funcname} of the class: {self.classname}')
        try:
            z = np.abs(stats.zscore(self.data[self.numerical_feature]))
            threshold = 3
            data_clean = self.data[(z < 3).all(axis=1)]
            self.logger_object.log(self.file_object, f'Successfully Handled outliers using Z-Score in the columns: {numerical_feature}')
            self.logger_object.log(self.file_object, f'Exited the function: {self.funcname} of the class: {self.classname}')
            return data_clean
        except Exception as e:
            self.logger_object.log(self.file_object,f"Exception occured in {self.funcname} method of {self.classname} class. Exception message: {e}",)
            self.logger_object.log(self.file_object, f'Exited the function: {self.funcname} of the class: {self.classname}')
            raise Exception()        
       
    #one hot encoding of categorical features
    def one_hot_encoding(self,data):
        self.funcname=self.one_hot_encoding.__name__
        self.data=data
        self.logger_object.log(self.file_object,f'Entered the function: {self.funcname} of the class: {self.classname}')
        try:
            cat_col=['type']
            data_cat = pd.get_dummies(self.data, columns=cat_col, drop_first=True)
            self.logger_object.log(self.file_object, f'Successfully Onehot encoded the categorical columns: {cat_col}')
            self.logger_object.log(self.file_object, f'Exited the function: {self.funcname} of the class: {self.classname}')
            return data_cat
        except Exception as e:
            self.logger_object.log(self.file_object,f"Exception occured in {self.funcname} method of {self.classname} class. Exception message: {e}",)
            self.logger_object.log(self.file_object, f'Exited the function: {self.funcname} of the class: {self.classname}')
            raise Exception()
   
    def scale_numerical_columns(self,data):
        """ This method scales the numerical values using the Standard scaler. """
        self.funcname=self.scale_numerical_columns.__name__
        self.logger_object.log(self.file_object,
                               'Entered the scale_numerical_columns method of the Preprocessor class')
        self.data=data

        try:
            self.num_df = self.data.select_dtypes(include=['int64']).copy()
            self.scaler = StandardScaler()
            self.scaled_data = self.scaler.fit_transform(self.num_df)
            self.scaled_num_df = pd.DataFrame(data=self.scaled_data, columns=self.num_df.columns)


            self.logger_object.log(self.file_object, 'Successfully Scaled the numerical values . Exited the scale_numerical_columns method of the Preprocessor class')
            return self.scaled_num_df

        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in scale_numerical_columns method of the Preprocessor class. Exception message:  ' + str(e))
            self.logger_object.log(self.file_object, 'scaling for numerical columns Failed. Exited the scale_numerical_columns method of the Preprocessor class')
            raise Exception()

    
    def handle_imbalanced_dataset(self,x,y):
        """ This method handles the imbalanced dataset to make it a balanced one. """
        self.funcname=self.handle_imbalanced_dataset.__name__
        self.logger_object.log(self.file_object,
                               'Entered the handle_imbalanced_dataset method of the Preprocessor class')

        try:
            x=np.array(x)
            y=y.ravel()
            self.rdsmple = RandomUnderSampler()
            self.x_sampled,self.y_sampled  = self.rdsmple.fit_resample(x,y)
            self.logger_object.log(self.file_object,
                                   'dataset balancing successful. Exited the handle_imbalanced_dataset method of the Preprocessor class')
            return self.x_sampled,self.y_sampled

        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in handle_imbalanced_dataset method of the Preprocessor class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'dataset balancing Failed. Exited the handle_imbalanced_dataset method of the Preprocessor class')
            raise Exception()
