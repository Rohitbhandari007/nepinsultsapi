import imp
from django.urls import path
from .views import getData


urlpatterns = [
    path('nepsultsapi/', getData, name="get-data"),
]
