from django.shortcuts import render
from .models import *

def index(request):
    enamels = Enamel.objects.all()
    print(enamels)
    return render(request, template_name='lab/index.html', context={'enamels': enamels})
