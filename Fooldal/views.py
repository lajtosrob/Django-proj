from django.shortcuts import render
from . models import Szemely

# Create your views here.

"""
def fooldal(request):
    egy_nev = 'Eszter'

    nevek_lista = ['Evi', 'Erzsi', 'Eszter', 'Hajnalka', 'Julianna', 'Viktória']

    nevek_szotar = {'Evi' : 25, 'Erzsi' : 33, 'Eszter' : 45, 'Hajnalka' : 31, 'Julianna' : 34, 'Viktória' : 32}


    return render(request, 'fooldal.html', {'nevek_lista': nevek_lista, 'nevek_szotar': nevek_szotar})
"""


def fooldal(request):
    szemelyek = Szemely.objects.filter(keresztnev__contains="e")
    return render(request, 'fooldal.html', {"szemelyek": szemelyek})