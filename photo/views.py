from django.shortcuts import render
from django.http import HttpResponse, Http404# responsible for returning a response to a user
import datetime as dt


# Create your views here.
def fashion(request):
    return render(request, 'fashion.html')

