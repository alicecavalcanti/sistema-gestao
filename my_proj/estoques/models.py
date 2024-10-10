
# Create your models here.
from django.db import models
from django.urls import reverse

class Estoque(models.Model):
    produto = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)
    validade = models.DateField()
    fornecedor = models.CharField(max_length=200)

    def __str__(self):
        return self.produto
