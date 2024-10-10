from django.urls import path
from . import views

urlpatterns = [
    path('', views.fornecedor_list, name='fornecedor_list'),
    path('view/<int:pk>', views.fornecedor_view, name='fornecedor_view'),
    path('new', views.fornecedor_create, name='fornecedor_new'),
    path('detail/<int:pk>', views.fornecedor_view, name='fornecedor_detail'),
    path('edit/<int:pk>', views.fornecedor_update, name='fornecedor_edit'),
    path('delete/<int:pk>', views.fornecedor_delete, name='fornecedor_delete'),
]