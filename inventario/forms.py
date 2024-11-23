from django import forms
from .models import Extintor

class ExtintorForm(forms.ModelForm):
    class Meta:
        model = Extintor
        fields = ['nombre', 'tipo', 'cantidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }