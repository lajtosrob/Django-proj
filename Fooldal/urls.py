from django.urls import path
from . import views

urlpatterns = [
    path('', views.fooldal, name='fooldal'),
    #path('rolunk/', views.rolunk)
    path('uj-szemely/', views.uj_szemely, name="uj-szemely")
]
