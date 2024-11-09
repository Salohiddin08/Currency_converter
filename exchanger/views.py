from asyncio.windows_events import NULL
from http.client import HTTPResponse
import json
from .models import currency
from django.shortcuts import render,HttpResponse
import requests
# Create your views here.
def home(request):

    e = currency.objects.all
    amount = NULL
    if request.method == 'POST':
        fc = request.POST.get('fcategory')
        tc = request.POST.get('tcategory')
        am = request.POST.get('amount')
    
        u = f'https://api.apilayer.com/fixer/convert?apikey=q8U7MEXFNiSDyOsbvMfWlP5nfv7wQ0gH&from={fc}&to={tc}&amount={am}'
        response = requests.get(u)
        result = response.json()
        amount = result['result']
        return render(request,'exchanger/home.html',{'cur':e,'camount':amount})

    return render(request,'exchanger/home.html',{'cur':e,'camount':amount})