#views 
#imports
from cgitb import html
from django import http
from django.http import HttpResponse
from django.shortcuts import render
import requests
import datetime
from .d import *
#for main page
def index(request):
    return render(request,'index.html')
#for about page
def about(request):
    return render(request,'about.html')
#for forecast page
def forecast(request):
    return render(request,'forecast.html')
#for contact page
def contact(request):
    return render(request,'contact.html')
#for python script
def d(request):
    return render(request,'d.py')
#for forecast button
def button(request):
    
    return render(request,'index.html')
#for output
def output(request):
    
    output_data = calculateCyclone();
    
    
    return render(request,"index.html",{"output_data":output_data})




