from django.http import HttpResponse
#from django.contrib.staticfiles,
from django.shortcuts import render

def home(request):
    return render(request,'home.html')