
# Money Laundering Prevention

To build a machine learning model that can identify the money laundering activities weather the transaction has occured is fraud or not.

## Table Content ✏️
* Demo
* Overview
* Dataset
* Installation
* Deployment
* Documentation
* Directory Tree
* Technology Used
* Bug/Feature Request
* Future scope of project
## Demo
Heroku:- https://visibility-prediction.herokuapp.com/

AWS(Ec2):- https://ec2-54-84-85-146.compute-1.amazonaws.com:5000 


## Overview  📜
The application is a web app which is developed in Flask Framework.
## Dataset  
Dataset available in kaggle: PaySim

https://www.kaggle.com/ealaxi/paysim1

We used PaySim synthetic dataset to train our ML model. It is based on a sample of real transactions extracted from one month of financial logs from a mobile money service implemented in an African country.
The original logs were provided by a multinational company, who is the provider of the mobile financial service which is currently running in more than 14 countries all around the world. This synthetic dataset is scaled down 1/4 of the original dataset.

This dataset contains 6362620 Transaction records with 11 features.

## Installations  🗄️
The Code is written in Python 3.8 If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:
```bash
  pip install -r requirements.txt
```
## Deployment

## Database 

## Tree Structure
```javascript
├── app_logger
│   ├──logger.py
├── log_file
│   ├── db_operation.txt
│   ├── Model_tarining.txt
├── templates
│   ├── database.html
│   ├── index.html
├── src
│   ├── model_train
│   ├── index.html
├── Money_Laundering_EDA.ipynb
├── XGB_Classifier.pkl
├── Procfile
├── data_preprocessing_.csv
├── app.py
├── requirements.txt
├── input_file.csv
├── README.md

```


## Documentation

[Architecture](https://linktodocumentation)

[Low Level Documentation](https://linktodocumentation)

[High Level Documentation](https://linktodocumentation)

[Wired Framed Diagram](https://linktodocumentation)

[DRP (Detailed Document Report)](https://linktodocumentation)
## Technologies Used

* Python
* FrontEnd: HTML & CSS
* Backend: Flask 
* Deployment : AWS, Heroku

## Contributers
You can feel free to reach out me at shubhammourya2014@gmail.com

@Shubham Mourya