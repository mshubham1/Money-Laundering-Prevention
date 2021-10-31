import numpy as np
from src.model_training import  trainModel
from flask import Flask, request, render_template
from app_logger.logger import App_Logger
from Database_Files.db_operation import Connector
from flask import Response
import joblib

app = Flask(__name__)
model = joblib.load(open("XGB_Classifier.pkl", "rb"))

#home route
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

#predict route
@app.route("/predict", methods=['POST','GET'])
def predict():
    if request.method == "POST":
        step = int(request.form.get('step'))
        amount = int(request.form.get('amount'))
        oldbalanceOrg = int(request.form.get('oldbalanceOrg'))
        oldbalanceDest = int(request.form.get('oldbalanceDest'))
        type1 = str(request.form.get('type'))
        CASH_IN=0
        CASH_OUT=0
        DEBIT=0
        PAYMENT=0
        TRANSFER=0
        if type1 == 'CASH_IN':
            CASH_IN=1
        elif type1 == 'CASH_OUT':
            CASH_OUT=1
        elif type1 == 'DEBIT':
            DEBIT=1
        elif type1 == 'PAYMENT':
            PAYMENT=1
        elif type1 == 'TRANSFER':
            TRANSFER=1
        input1 = {
                'step': step,
                'amount': amount,
                'oldbalanceOrg': oldbalanceOrg,
                'oldbalanceDest': oldbalanceDest,
                'trans_type': type1
                }
        
        #input1['step']=int(input1['step'])
        #input2=[[step,amount,oldbalanceOrg,oldbalanceDest,type1,CASH_IN,CASH_OUT,DEBIT,PAYMENT,TRANSFER]]
        file = open("log_file/Model_Training.txt", 'a+')
        logger = App_Logger()
        input2=np.array([[step,amount,oldbalanceOrg,oldbalanceDest,CASH_IN,CASH_OUT,DEBIT,PAYMENT,TRANSFER]])
        trainModelObj = trainModel() #object initialization
        trainModelObj.trainingModel(input1)
        output=model.predict(input2)
        
        logger.log(file, 'Prediction done successfully !!')
        file.close()
        if output==1:
             return render_template('index.html',result="The transaction is fraud!! Be Aware.")
        else:
            return render_template('index.html',result="You are safe The trsaction is not Fraud.")

        
    else:
        return render_template('index.html')


@app.route("/database", methods = ['GET','POST'])
def test():
    heading = ('uuid','step', 'amount','oldbalanceOrg', 'oldbalanceDest' , 'trans_type')
    data = Connector()
    return render_template('database.html', heading=heading, data=data.getData())

if __name__ == "__main__":
    app.run(debug=True)