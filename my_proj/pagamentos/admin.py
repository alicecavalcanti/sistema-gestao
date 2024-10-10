from django.contrib import admin

# Register your models here.
from django.contrib import admin
from pagamentos.models import Pagamento

admin.site.register(Pagamento)
