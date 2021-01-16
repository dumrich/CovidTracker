from django.shortcuts import render
from .tracker import Tracker

Tracker = Tracker()
Tracker.parse_into_dict()

def index(request):
    return render(request,
                  'track/general.html')
