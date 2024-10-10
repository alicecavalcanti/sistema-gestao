from django.contrib import admin

# Register your models here.
from django.contrib import admin
from pedidos.models import Pedido

admin.site.register(Pedido)
