"""
Views are Python functions that take requests and return responses.
"""

from django.shortcuts import render
from django.http import JsonResponse
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

        latest_forecast = {} #Dict to to save data with the latest forecast date

        for dataset in forecasts:
            if conv_comp_id == dataset.company_id and dataset.forecast_date <= conv_date: #Filtering criteria
                
                #Detects the latest forecast date and puts data in latest_forecast dict
                if (conv_comp_id not in latest_forecast or dataset.forecast_date > latest_forecast[conv_comp_id].forecast_date):
                    latest_forecast[conv_comp_id] = dataset
                    print (latest_forecast[conv_comp_id])

        #Saves the forecast values starting from the queried param date in a list.
        if latest_forecast:
            dataset = latest_forecast[conv_comp_id]
            date_offset = (conv_date - dataset.forecast_date).days

            for filtered_values in range(date_offset, len(dataset.values)):
                data = dataset.values[filtered_values]
                datalist.extend({data})
                
        #If List is empty => no Forecast Values were found
        if not datalist:
            return JsonResponse({"Response":{"Values": "No Forecast Values found"}})

        #Returns the correct Forecast Values
        return JsonResponse({"Response":{"Forecast Values": datalist}})

    #Invalid Query Param Input
    except ValueError:
        return JsonResponse({"Response":{"Forecast Values": "Your input was not valid"}})
    
    