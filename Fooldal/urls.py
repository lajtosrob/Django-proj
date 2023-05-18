from django.urls import path
from . import views

urlpatterns = [
    path('', views.fooldal, name='fooldal'),
    path('szemelyek', views.szemelyek, name='szemelyek'),
    #path('rolunk/', views.rolunk)
    path('uj-szemely/', views.uj_szemely, name="uj-szemely"),
    path('rolunk/', views.rolunk, name="rolunk"),
    path('kapcsolat/', views.kapcsolat, name="kapcsolat"),

]
