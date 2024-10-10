from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from pedidos.models import Pedido

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'preco', 'tipo', 'descricao']

def pedido_list(request, template_name='pedidos/pedido_list.html'):
    pedido = Pedido.objects.all()
    data = {}
    data['object_list'] = pedido
    return render(request, template_name, data)

def pedido_view(request, pk, template_name='pedidos/pedido_detail.html'):
    pedido= get_object_or_404(Pedido, pk=pk)    
    return render(request, template_name, {'object':pedido})

def pedido_create(request, template_name='pedidos/pedido_form.html'):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pedido_list')
    return render(request, template_name, {'form':form})

def pedido_update(request, pk, template_name='pedidos/pedido_form.html'):
    pedido= get_object_or_404(Pedido, pk=pk)
    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
        form.save()
        return redirect('pedido_list')
    return render(request, template_name, {'form':form})

def pedido_delete(request, pk, template_name='pedidos/pedido_confirm_delete.html'):
    pedido= get_object_or_404(Pedido, pk=pk)    
    if request.method=='POST':
        pedido.delete()
        return redirect('pedido_list')
    return render(request, template_name, {'object':pedido})