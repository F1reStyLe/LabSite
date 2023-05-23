from django import forms
from .models import PigmentPaste, Pigment, Enamel


class PigmentPasteForm(forms.ModelForm):
    class Meta:
        model = PigmentPaste
        fields = ('name', 'base', 'pigment',)


class PigmentForm(forms.ModelForm):
    class Meta:
        model = Pigment
        fields = ('name', 'pigment_group',)


class Enamel(forms.ModelForm):
    class Meta:
        model = Enamel
        fields = ('name', 'color', 'base', 'pigment_paste')