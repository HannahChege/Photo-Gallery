from django.shortcuts import render
from django.http import HttpResponse, Http404# responsible for returning a response to a user
import datetime as dt
from .models import 

# Create your views here.
def welcome(request):
    return HttpResponse('Fashion')

