from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics  import confusion_matrix, accuracy_score, classification_report
import pandas as pd

class Model_Finder:
    """  This class shall  be used to find the model with best accuracy and AUC score."""

    def __init__(self,file_object,logger_object):
        self.file_object = file_object
        self.logger_object = logger_object
        self.models_dict = {
            "Logistic Regression": LogisticRegression(),
            "Random Forest Classifier": RandomForestClassifier(),
            "SVC Classifier": SVC(),
            "XGBClassifier": XGBClassifier(),
            "K Neighbors Classifier": KNeighborsClassifier(),
            "GaussianNB": GaussianNB(),
        }
        self.gnb = GaussianNB()
        self.logistic = LogisticRegression()
        self.knn = KNeighborsClassifier()
        self.svc = SVC()
        self.rf = RandomForestClassifier()
        self.xgb = XGBClassifier(objective='binary:logistic',n_jobs=-1)


    def get_best_params_for_xgboost(self,X_train,y_train):

        """ get the parameters for XGBoost Algorithm which give the best accuracy.Use Hyper Parameter Tuning."""
        self.logger_object.log(self.file_object,
                               'Entered the get_best_params_for_xgboost method of the Model_Finder class')
        try:
            # initializing with different combination of parameters
            self.param_grid_xgboost = {


            }
            # Creating an object of the Grid Search class
            self.grid= GridSearchCV(XGBClassifier(objective='binary:logistic'),self.param_grid_xgboost, verbose=3,cv=5)
            # finding the best parameters
            self.grid.fit(X_train, y_train)

            # extracting the best parameters
            self.criterion = self.grid.best_params_['criterion']
            self.max_depth = self.grid.best_params_['max_depth']
            self.n_estimators = self.grid.best_params_['n_estimators']

            # creating a new model with the best parameters
            self.xgb = XGBClassifier(criterion=self.criterion, max_depth=self.max_depth,n_estimators= self.n_estimators, n_jobs=-1 )
            # training the mew model
            self.xgb.fit(X_train, y_train)
            self.logger_object.log(self.file_object,
                                   'XGBoost best params: ' + str(
                                       self.grid.best_params_) + '. Exited the get_best_params_for_xgboost method of the Model_Finder class')
            return self.xgb
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in get_best_params_for_xgboost method of the Model_Finder class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'XGBoost Parameter tuning  failed. Exited the get_best_params_for_xgboost method of the Model_Finder class')
            raise Exception()


    def get_best_model(self,X_train,y_train,X_test,y_test):
        """ Find out the Model which has the best AUC score. """
        self.logger_object.log(self.file_object,
                               'Entered the get_best_model method of the Model_Finder class')       
        try:
            self.metrics = {"models": []}
            for model_name, training_model in self.models_dict.items():
                model=training_model.fit(X_train,y_train)
                self.logger_object.log(self.file_object, f"Successfully trained {model} model.")

                y_pred = model.predict(X_test)
                
                accuracy = accuracy_score(y_test, y_pred)
                confusion_matrix1 = confusion_matrix(y_test, y_pred)
                classfication = classification_report(y_test,y_pred)
                self.logger_object.log(self.file_object, f"Successfully calculated the Accuracy score, confusion matrix and classification_report for {model} model.")

                self.metrics["models"].append(
                    {"model_name": model_name, "accuracy_score": accuracy, "confusion_matrix": confusion_matrix1, "classification_report":classfication}
                )
                self.logger_object.log(self.file_object,"Successfully appended model name and model metrics as a dictionary.",  )
            df=pd.read_json(self.metrics)
            df.to_json("models/metrics.json")
            
            self.xgboost= self.get_best_params_for_xgboost(X_train,y_train)
            self.prediction_xgboost = self.xgboost.predict(X_test) # Predictions using the XGBoost Model

            if len(y_test.unique()) == 1: #if there is only one label in y, then roc_auc_score returns error. We will use accuracy in that case
                self.xgboost_score = accuracy_score(y_test, self.prediction_xgboost)
                self.logger_object.log(self.file_object, 'Accuracy for XGBoost:' + str(self.xgboost_score))  # Log AUC
        
            return 'XGB_Classifier',self.xgboost
    

        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occured in get_best_model method of the Model_Finder class. Exception message:  ' + str(
                                       e))
            self.logger_object.log(self.file_object,
                                   'Model Selection Failed. Exited the get_best_model method of the Model_Finder class')
            raise Exception()

