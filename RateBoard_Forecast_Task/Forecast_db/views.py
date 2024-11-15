"""
Views are Python functions that take requests and return responses.
"""

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Forecast

# Create your views here.
def forecast_view(request):
    
    forecasts = Forecast.objects.all()
    datalist=[]
    for dataset in forecasts:
        data = {"id":dataset.id, "company_id": dataset.company_id, "forecast_date":dataset.forecast_date, "values": dataset.values}   
        datalist.append(data)
    
    return JsonResponse({"datasets": datalist})