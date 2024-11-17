# Forecast Project Protocoll

## About the Project
This project involves developing a backend using the Django framework. A database will be created and populated with data. Additionally, an API will be built to interact with this database.

The database will contain the following fields: id(Autoincrement), company_id, forecast_date, and a list of values. Using query parameters (date and company_id) passed in the API endpoint, the forecast values are returned from the specified start date and depending on the last forecast date.

The filtering criteria are as follows: forecast_date <= the provided date parameter and company_id == company_id query parameter.

## Getting Started
The main features of the Forecast App are outlined below, including project setup and configuration, database creation using Django models, and the Python API logic for filtering database content.

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
The migrate command pushes the changes to the Database.

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

### Python Forecast Logic
The Forecast API Logic is the heart of this Project. It filtered and outputs the correct forecast Values.

```python
def forecast_view(request):

    #fetches the query param defined in postman
    comp_id = request.GET.get('company_id')
    date_str = request.GET.get('date')

    forecasts = Forecast.objects.all() #Problem if there are many datasets (Performance)
    forcast_values_list=[]

    try:
        conv_comp_id = int(comp_id)
        conv_date = datetime.strptime(date_str, '%Y-%m-%d').date()

        latest_forecast = {} #Dict to to save data with the latest forecast date

        for dataset in forecasts:
            if conv_comp_id == dataset.company_id and dataset.forecast_date <= conv_date: #Filtering criteria
                
                #Detects the latest forecast date and puts data in latest_forecast dict
                if (conv_comp_id not in latest_forecast or dataset.forecast_date > latest_forecast[conv_comp_id].forecast_date):
                    latest_forecast[conv_comp_id] = dataset

        #Saves the forecast values starting from the queried param date in a list.
        if latest_forecast:
            dataset = latest_forecast[conv_comp_id]
            date_offset = (conv_date - dataset.forecast_date).days

            #Filters values based on the offset and extend it to the list
            for filtered_values in range(date_offset, len(dataset.values)):
                data = dataset.values[filtered_values]
                forcast_values_list.extend({data})
                
        #If List is empty => no Forecast Values were found
        if not forcast_values_list:
            return JsonResponse({"Response":{"Values": "No Forecast Values found"}})

        #Returns the correct Forecast Values
        return JsonResponse({"Response":{"Forecast Values": forcast_values_list}})

    #Invalid Query Param Input
    except ValueError:
        return JsonResponse({"Response":{"Forecast Values": "Your input was not valid"}})
```
### API with Postman
The API developed in this project is tested using Postman. The endpoint is accessed via a GET request with two query parameters.

#### Postman Request
![grafik](https://github.com/user-attachments/assets/b9d37160-97d9-4cee-9c47-b86b47b4ab40)

#### Postman Responses
The logic contains 3 response options: ‘Forecast Values Found’, ‘No Forecast Values Found’ and ‘Invalid Input’:

![grafik](https://github.com/user-attachments/assets/09fec8b5-f0bb-4246-bd48-68b73453920e)

![grafik](https://github.com/user-attachments/assets/967079ed-7f3b-43f1-9dd2-8ca4331f5ea5)

![grafik](https://github.com/user-attachments/assets/059e63d2-de42-4ae9-97f4-94d868f3f0b7)

## Quality of software

### Maintainability

The Django framework ensures good maintainability by organizing each component into dedicated sections, such as models, views, URLs, and more. Additionally, maintainability is supported through  code commenting and a readable code structure.

The framework also allows for easy extensibility, making it straightforward to add new models, functions in views.py, or new endpoints as needed.

### Scalability

Scalability describes when a programm is enlarged so that the performance stays the same, if possible.
The current program would therefore have to be optimised if for example several data records are written to the database so that the performance remains as constant as possible.

### Performance

Performance and Scalability are closly connected to each other. The performance is the main point of the Scalability. The goal for every program is to optimize your code for a better performance.

## Problems with this Setup!

The more data records are loaded into the database, the greater the filtering effort. This means that more data records have to be checked and performance will suffer as a result. 
If more data records are written to the database, the database becomes more complex. In this case, you should consider a different database design. The basic principles (persistence, consistency, avoidance of redundancies, security, integrity and efficiency) should be retained.

## Conclusion
The conclusion from this project is that the development of the API has been successful so far and is working. The code is understandable and has been sufficiently commented. The database design was kept simple and all required fields were configured.

There would be room for improvement when loading the database object in the views.py section:
```python
forecasts = Forecast.objects.all() #Problem if there are many datasets (Performance)
```
Instead of loading all records, it would be more efficient to filter the required data directly, avoiding unnecessary data retrieval.

Another problem at the beginning was that the task was misunderstood and the entire data records were always output regardless of the query parameter date.
The values should actually be outputed depending on the latest forecast date and the date query parameter.
But despite some problems at the beginning, the task was accomplished.
