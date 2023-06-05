from django.shortcuts import render
from rest_framework import generics

from .sirializer import EnamelSerializer
from lab.models import Enamel

class EnamelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Enamel.objects.all().select_related('base')
    serializer_class = EnamelSerializer