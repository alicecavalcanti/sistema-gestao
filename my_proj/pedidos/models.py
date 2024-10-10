from django.db import  models
from django.urls import reverse

class Pedido(models.Model):
    cliente = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.CharField(max_length=20, default=" ")
    descricao = models.CharField(max_length=200, default=" ")
    def __str__(self):
        return self.cliente

    def get_absolute_url(self):
        return reverse('pedido_edit', kwargs={'pk': self.pk})




