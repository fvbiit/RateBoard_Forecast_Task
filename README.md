# Forecast Project Protocoll

## About the Project
This project involves the development of a backend with the Django framework. A database is to be created and filled with data. Furthermore, an API is to be developed that communicates with this database. The database contains: ‘company_id, “forecast_date” and a list of “values”. With the help of query parameters (‘date’ and ‘company_id’), which are passed in the endpoint, the forecast values are to be printed in the form of values. 
The filter requirement is as follows: forecast_date <= queried param date and company_id == queried param company_id

## Getting Started
The main points of the Forecast App are described below, such as project creation and configurations, as well as the creation of the database using models and the Python logic for filtering the database contents.

### Create Django Project 

```sh
django-admin startproject RateBoard_Forecast_Task
```
### Create an App inside the Django Project

```sh
py manage.py startapp Forecast_db
```
### Design the Model for the Database

```python
from django.db import models #Libraries

"""
Create a Model-Class "Forecast" for Database and define the behaviour for the Datasets. 
"""
class Forecast(models.Model):

    #Datasets
    company_id = models.IntegerField()
    forecast_date = models.DateField()
    values = models.JSONField() #Create List or Dict

    #Str Function for Object Output.
    def __str__(self):
        return f"ID: {self.id}, Company_ID: {self.company_id}, Forecast Date: {self.forecast_date}, Values: {self.values}"
```
### Migrations
#### Makemigartion

```sh
python manage.py makemigrations
```
The makemigrations command creates a migration file. A migration file consists of Python code that represents the database changes such as creating a new table, setting new fields, ....

#### Migrate

```sh
python manage.py migrate
```
The migrate command pushes the changes to the Database

#### Define Datasets with the Python Shell

```sh
>>>from Forecast_db.models import Forecast
>>>record_1 = Forecast(company_id=1, forecast_date="2024-01-01", values=[1,2,3,4]
>>>record_1.save()
>>>record_1
<Forecast: ID: 1, Company_ID: 1, Forecast Date: 2024-01-01, Values: [1,2,3,4]>

>>>record_2 = Forecast(company_id=1, forecast_date="2024-01-03", values=[5,6,7,8]
>>>record_2.save()
>>>record_2
<Forecast: ID: 2, Company_ID: 1, Forecast Date: 2024-01-03, Values: [5,6,7,8]>

>>>record_3 = Forecast(company_id=2, forecast_date="2024-12-01", values=[1.1,2.2,3.3,4.4]
>>>record_3.save()
>>>record_3
<Forecast: ID: 3, Company_ID: 2, Forecast Date: 2024-12-01, Values: [1.1,2.2,3.3,4.4]>

>>>record_4 = Forecast(company_id=2, forecast_date="2024-12-03", values=[5.5,6.6,7.7,8.8]
>>>record_4.save()
>>>record_4
<Forecast: ID: 4, Company_ID: 2, Forecast Date: 2024-12-03, Values: [5.5,6.6,7.7,8.8]>
```
### Database
![grafik](https://github.com/user-attachments/assets/1c5ac264-5d08-4c9c-a287-e8bce04cfb6f)


