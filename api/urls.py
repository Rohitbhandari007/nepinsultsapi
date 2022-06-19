import imp
from django.urls import path
from .views import getData


urlpatterns = [
    path('api/', getData, name="get-data"),
]
