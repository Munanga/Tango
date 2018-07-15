from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'index.html', context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page on real.<br><a href='/rango/'>Main page</a>")