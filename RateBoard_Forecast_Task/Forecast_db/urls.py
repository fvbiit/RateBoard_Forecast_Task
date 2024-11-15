from django.urls import path
from . import views

urlpatterns = [
    path('Forecast/', views.forecast_view, name="Forecast"),
]