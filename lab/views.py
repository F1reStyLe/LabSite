from django.shortcuts import render
from .models import *

def index(request):

    return render(request, template_name='lab/index.html')


def sample_list(request):
    samples = PigmentPaste.objects.all()
    return render(request, template_name='lab/sample_list.html', context={'samples': samples})


def add_sample(request):
    return render(request, template_name='lab/sample_list.html')


def sample(request, pk):
    analysis = Analysis.objects.filter(sample__id=pk)
    sample = PigmentPaste.objects.get(id=pk)
    return render(request, template_name='lab/sample.html', context={'analysis': analysis, 'sample': sample,})


def contacts(request):
    
    return render(request, template_name='lab/contacts.html')

