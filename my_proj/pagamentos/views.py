from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from pagamentos.models import Pagamento

class PagamentoForm(ModelForm):
    class Meta:
        model = Pagamento
        fields = ['data', 'valor', 'metodo']

def pagamento_list(request, template_name='pagamentos/pagamento_list.html'):
    pagamento = Pagamento.objects.all()
    data = {}
    data['object_list'] = pagamento
    return render(request, template_name, data)

def pagamento_view(request, pk, template_name='pagamentos/pagamento_detail.html'):
    pagamento= get_object_or_404(Pagamento, pk=pk)    
    return render(request, template_name, {'object':pagamento})

def pagamento_create(request, template_name='pagamentos/pagamento_form.html'):
    form = PagamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pagamento_list')
    return render(request, template_name, {'form':form})

def pagamento_update(request, pk, template_name='pagamentos/pagamento_form.html'):
    pagamento= get_object_or_404(Pagamento, pk=pk)
    form = PagamentoForm(request.POST or None, instance=pagamento)
    if form.is_valid():
        form.save()
        return redirect('pagamento_list')
    return render(request, template_name, {'form':form})

def pagamento_delete(request, pk, template_name='pagamentos/pagamento_confirm_delete.html'):
    pagamento= get_object_or_404(Pagamento, pk=pk)    
    if request.method=='POST':
        pagamento.delete()
        return redirect('pagamento_list')
    return render(request, template_name, {'object':pagamento})
