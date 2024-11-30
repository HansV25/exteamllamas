from django import forms
from django.contrib.auth.models import User
from .models import Perfil
from django.contrib.auth.password_validation import validate_password

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password_confirmacion = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')
    rol = forms.ChoiceField(choices=Perfil.ROLES, label='Rol')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirmacion']
        widgets = {
            'password': forms.PasswordInput,
        }
        help_texts = {
            'password': "La contraseña debe tener al menos 8 caracteres, incluyendo mayúsculas, minúsculas, números y símbolos.",
        }

    def clean_password_confirmacion(self):
        password = self.cleaned_data.get('password')
        password_confirmacion = self.cleaned_data.get('password_confirmacion')
        if password and password_confirmacion and password != password_confirmacion:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirmacion

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password
