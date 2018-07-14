from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hooowdy Man!!</h1>")

def about(request):
    return HttpResponse("Rango says here is the about page on real.<br><a href='/rango/'>Main page</a>")