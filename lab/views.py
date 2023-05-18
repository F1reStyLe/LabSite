from django.shortcuts import render
from .models import *

def index(request):

    return render(request, template_name='lab/index.html')
