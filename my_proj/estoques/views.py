from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from estoques.models import Estoque

class EstoqueForm(ModelForm):
    class Meta:
        model = Estoque
        fields = ['produto', 'quantidade', 'validade', 'fornecedor']

def estoque_list(request, template_name='estoques/estoque_list.html'):
    estoque = Estoque.objects.all()
    data = {}
    data['object_list'] = estoque
    return render(request, template_name, data)

def estoque_view(request, pk, template_name='estoques/estoque_detail.html'):
    estoque= get_object_or_404(Estoque, pk=pk)    
    return render(request, template_name, {'object':estoque})

def estoque_create(request, template_name='estoques/estoque_form.html'):
    form = EstoqueForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('estoque_list')
    return render(request, template_name, {'form':form})

def estoque_update(request, pk, template_name='estoques/estoque_form.html'):
    estoque= get_object_or_404(Estoque, pk=pk)
    form = EstoqueForm(request.POST or None, instance=estoque)
    if form.is_valid():
        form.save()
        return redirect('estoque_list')
    return render(request, template_name, {'form':form})

def estoque_delete(request, pk, template_name='estoques/estoque_confirm_delete.html'):
    estoque= get_object_or_404(Estoque, pk=pk)    
    if request.method=='POST':
        estoque.delete()
        return redirect('estoque_list')
    return render(request, template_name, {'object':estoque})
