from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'index.html', context_dict)

def about(request):
    cont = {'message':"Rango says here is the about page on real."}
    return render(request,'about.html',cont)