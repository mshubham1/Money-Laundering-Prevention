
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

* Web
![pic1](https://user-images.githubusercontent.com/47842305/139574877-0f69b2d6-b1cc-4c57-9871-d36c5521425d.png)
![pic2](https://user-images.githubusercontent.com/47842305/139574888-6834b33d-0913-4a42-9a15-e3cea6f399ac.png)


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

# Heroku
App is deployed in the heroku login. 
![image](https://user-images.githubusercontent.com/47842305/139574946-ccf9a882-93ac-4379-86c4-8562b00050bb.png)

# AWS
App is deployed in the AWS EC2 instance for free tier.
![image](https://user-images.githubusercontent.com/47842305/139574951-4d9f1732-456c-4862-b9c0-84f673c7f6b7.png)

* Database
![pic3](https://user-images.githubusercontent.com/47842305/139574890-9579d928-05cb-4f5a-a345-b94de7c4edff.png)

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
│   ├── data_preprocessing.py
│   ├── model_training.py
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

![image](https://user-images.githubusercontent.com/47842305/139575209-6e90151b-be8c-4ff1-97d9-a7ff5f6b7d94.png)
![image](https://user-images.githubusercontent.com/47842305/139575214-64b5b442-45f6-4d3e-b397-1deb869704e1.png)
![image](https://user-images.githubusercontent.com/47842305/139575215-59c28f81-73f4-4f5d-8e2a-7893b3204fcc.png)
![image](https://user-images.githubusercontent.com/47842305/139575216-01043b7b-1ee9-4ec0-a422-baa146a8555c.png)
![image](https://user-images.githubusercontent.com/47842305/139575314-975efc25-c9fa-42e4-9ebe-bb4331adfe59.png)


## Contributers
You can feel free to reach out me at shubhammourya2014@gmail.com

@Shubham Mourya
