"""
Views are Python functions that take requests and return responses.
"""

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Forecast
from datetime import datetime

# Create your views here.

def forecast_view(request):

    #fetches the query param defined in postman
    comp_id = request.GET.get('company_id')
    date_str = request.GET.get('date')


    forecasts = Forecast.objects.all() #Problem if there are many datasets (Performance)
    datalist=[]

    try:
        conv_comp_id = int(comp_id)
        conv_date = datetime.strptime(date_str, '%Y-%m-%d').date()

        for dataset in forecasts:
            if conv_comp_id == dataset.company_id and dataset.forecast_date <= conv_date:
                date_offset = (conv_date - dataset.forecast_date).days
                
                for filtered_values in range(date_offset, len(dataset.values)):
                    data = dataset.values[filtered_values]
                    datalist.extend({data})

        if not datalist:
            return JsonResponse({"Values": "No Forecast Values found"})
        
        return JsonResponse({"Values": datalist})
    
    except ValueError:
        return JsonResponse({"Values": "Your input was not valid"})
    
    