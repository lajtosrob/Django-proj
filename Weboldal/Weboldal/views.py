
from django.http import HttpResponse

def szia(request):
    return HttpResponse("<h1>Szia, Szia, Szia!</h1>")

def hello(request):
    return HttpResponse("<h1>Hello, Hello, Hello</h1>")

def home(request):
    return HttpResponse("<h1>This is my home page</h1>")