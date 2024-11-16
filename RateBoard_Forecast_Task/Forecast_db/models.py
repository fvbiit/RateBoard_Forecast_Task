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