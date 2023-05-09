
#from django.http import HttpResponse
from django.shortcuts import render

def fooldal(request):
    return render(request, 'fooldal.html')


def rolunk(request):
    return render(request, 'rolunk.html')



















"""
def szia(request):
    return HttpResponse("<h1>Szia, Szia, Szia!</h1>")

def hello(request):
    return HttpResponse("<h1>Hello, Hello, Hello</h1>")

def home(request):
    return HttpResponse("<h1>This is my home page</h1>")
"""
