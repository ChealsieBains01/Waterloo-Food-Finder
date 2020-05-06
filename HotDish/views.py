import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

url = 'https://api.uwaterloo.ca/v2/foodservices/menu.json'
params = {
    'key': settings.MENU_API_KEY,
}
r = requests.get(url, params=params)
data = r.json()['data']

def home(request):
    for i in data:
        if(data['date']['week'] == 1):
            print(data['date']['week'])
    return render(request, 'HotDish/home.html')
def brubakers(request):
    return render(request, 'HotDish/restaurant.html')
def V1(request):
    return render(request, 'HotDish/restaurant.html')
def REV(request):
    return render(request, 'HotDish/restaurant.html')
def CMH(request):
    return render(request, 'HotDish/restaurant.html')
def SCH(request):
    return render(request, 'HotDish/restaurant.html')

# Create your views here.
