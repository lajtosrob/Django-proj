from django.urls import path
from . import views

urlpatterns = [
    path('', views.fooldal),
    path('rolunk/', views.rolunk)
]
