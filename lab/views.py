from django.shortcuts import render
from .models import *
from .forms import *

def index(request):

    return render(request, template_name='lab/index.html')


def sample_list(request):
    samples = PigmentPaste.objects.all()
    return render(request, template_name='lab/sample_list.html', context={'samples': samples})


def add_sample(request):
    if request.method == 'POST':
        form = PigmentPasteForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return render(request, template_name='lab/add_sample.html')
    else:
        form = PigmentPasteForm()
    return render(request, template_name='lab/add_sample.html', context={'form': form})


def sample(request, pk):
    analysis = Analysis.objects.filter(sample__id=pk)
    sample = PigmentPaste.objects.get(id=pk)
    return render(request, template_name='lab/sample.html', context={'analysis': analysis, 'sample': sample,})


def contacts(request):
    
    return render(request, template_name='lab/contacts.html')

