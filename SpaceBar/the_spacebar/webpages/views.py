from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def apis(request):
    return render(request, 'webpages/apis.html')

def pictures (request):
    return render (request,'webpages/pictures.html')    

def wiki (request):
    return render (request, "webpages/wiki.html")

def data_science (request):
    return render (request, "webpages/wiki.html")