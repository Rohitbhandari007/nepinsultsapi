from django.shortcuts import render
from .models import Insults

def home(request):
    insults = Insults.objects.all()
    context = {
        'insults':insults
    }

    return render(request, 'core/index.html', context)
