from django.urls import path
from . import views

app_name = 'track'

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:country>/data/<str:region>', views.findCountryData, name="FindCountryData")
]
