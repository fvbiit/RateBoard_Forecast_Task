from django.db import models

# Create your models here.

class Forecast(models.Model):
    company_id = models.IntegerField()
    forecast_date = models.DateField()
    values = models.JSONField()

    def __str__(self):
        return f"{self.id} {self.company_id} {self.forecast_date} {self.values}"