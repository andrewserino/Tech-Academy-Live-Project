from django.urls import path

from . import views

urlpatterns = [
    path('', views.suntracker, name='suntracker')
]