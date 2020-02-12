from django.shortcuts import render
from django.http import HttpResponse

def index(req):
	return HttpResponse("polls index")
# Create your views here.
