from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'item_inventario', 'cantidad', 'fecha_entrega']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'item_inventario': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_entrega': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
