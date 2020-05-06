import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

url = 'https://api.uwaterloo.ca/v2/foodservices/locations.json'
params = {
    'key': settings.MENU_API_KEY,
}
r = requests.get(url, params=params)
data = r.json()['data']

def home(request):
    return render(request, 'Directory/Directory.html')