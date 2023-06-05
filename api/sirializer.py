from rest_framework import serializers
from lab.models import *



class EnamelSerializer(serializers.ModelSerializer):
    base = serializers.SlugRelatedField(slug_field='name', queryset=Base.objects)
    pigment_paste = serializers.SlugRelatedField(slug_field='name', queryset=PigmentPaste.objects)
    
    class Meta:
        model = Enamel
        fields = ['id', 'name', 'colour', 'base', 'pigment_paste']