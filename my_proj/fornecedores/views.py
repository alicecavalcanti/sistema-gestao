from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from fornecedores.models import Fornecedor

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'telefone', 'email']

def fornecedor_list(request, template_name='fornecedores/fornecedor_list.html'):
    fornecedor = Fornecedor.objects.all()
    data = {}
    data['object_list'] = fornecedor
    return render(request, template_name, data)

def fornecedor_view(request, pk, template_name='fornecedores/fornecedor_detail.html'):
    fornecedor= get_object_or_404(Fornecedor, pk=pk)    
    return render(request, template_name, {'object':fornecedor})

def fornecedor_create(request, template_name='fornecedores/fornecedor_form.html'):
    form = FornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fornecedor_list')
    return render(request, template_name, {'form':form})

def fornecedor_update(request, pk, template_name='fornecedores/fornecedor_form.html'):
    fornecedor= get_object_or_404(Fornecedor, pk=pk)
    form = FornecedorForm(request.POST or None, instance=fornecedor)
    if form.is_valid():
        form.save()
        return redirect('fornecedor_list')
    return render(request, template_name, {'form':form})

def fornecedor_delete(request, pk, template_name='fornecedores/fornecedor_confirm_delete.html'):
    fornecedor= get_object_or_404(Fornecedor, pk=pk)    
    if request.method=='POST':
        fornecedor.delete()
        return redirect('fornecedor_list')
    return render(request, template_name, {'object':fornecedor})