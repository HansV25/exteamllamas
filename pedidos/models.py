from django.db import models
from django.db import models
from Clientes.models import Cliente
from inventario.models import Extintor

# Create your models here.

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    item_inventario = models.ForeignKey(Extintor, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_entrega = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nombre}"
