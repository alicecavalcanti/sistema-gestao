from django.db import models

# Create your models here.

class Pagamento(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=100) 

    def __str__(self):
        return f"Pagamento de R$ {self.valor} em {self.data} - {self.metodo}"
