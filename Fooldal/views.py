from django.shortcuts import render, redirect
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
    szemelyek = Szemely.objects.all()
    return render(request, 'fooldal.html', {"szemelyek": szemelyek})

def uj_szemely(request):
    if request.method == "GET":
        return render(request, 'uj_szemely.html')
    elif request.method == "POST":
        veznev = request.POST.get('veznev')
        kernev = request.POST.get('kernev')
        kor = request.POST.get('kor')
        hazas = request.POST.get('hazas') # returns on or None
        tortenet = request.POST.get('tortenet')

        if hazas == 'on':
            hazas = True
        else:
            hazas = False

        szemely = Szemely(vezeteknev=veznev, keresztnev=kernev, eletkor=kor, hazas=hazas, elettortenet=tortenet)    
        szemely.save()
        

        return redirect('fooldal')