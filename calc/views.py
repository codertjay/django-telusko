from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path,include
from django.conf.urls import url


# Create your views here.

def home(request):
    return HttpResponse("Hello world")
