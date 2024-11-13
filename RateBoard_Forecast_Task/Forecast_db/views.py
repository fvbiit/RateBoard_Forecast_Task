"""
Views are Python functions that take requests and return responses.
"""

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("Hello world!")