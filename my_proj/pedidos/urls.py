from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedido_list, name='pedido_list'),
    path('view/<int:pk>', views.pedido_view, name='pedido_view'),
    path('new', views.pedido_create, name='pedido_new'),
    path('detail/<int:pk>', views.pedido_view, name='pedido_detail'),
    path('edit/<int:pk>', views.pedido_update, name='pedido_edit'),
    path('delete/<int:pk>', views.pedido_delete, name='pedido_delete'),
]