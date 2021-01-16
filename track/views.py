from django.shortcuts import render, redirect
from .tracker import Tracker
from django.http import HttpResponse

Tracker = Tracker()
Tracker.parse_into_dict()

def index(request):
    """Index View"""    
    if request.method=="POST":
        query = request.POST["country"].replace(" ", "").lower()
        return redirect(f'/{query}/data')
    return render(request,
                  'track/general.html')

def findCountryData(request, country):
    """Find Country View"""
    DataDict = Tracker.find_country(country=country)
    parallelData = zip(DataDict["Date"][::-1], DataDict["New Cases"][::-1], DataDict["Total Cases"][::-1], DataDict["New Deaths"][::-1], DataDict["Total Deaths"][::-1])
    if request.method=="POST":
        query = request.POST["country"].replace(" ", "").lower()
        return redirect(f'/{query}/data')
    return render(request,
                  'track/country.html',
                  {'country':country,
                   'Data':parallelData})
