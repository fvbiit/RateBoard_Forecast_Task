from django.urls import path
from . import views

urlpatterns = [
    path('Forecast/', views.test, name="test"),
]