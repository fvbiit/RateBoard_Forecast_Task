from django.db import models

# Create your models here.

class Forecast(models.Model):
    company_id = models.IntegerField()
    forecast_date = models.DateField()
    values = models.JSONField()

    def __str__(self):
        return f"ID: {self.id}, Company_ID: {self.company_id}, Forecast Date: {self.forecast_date}, Values: {self.values}"