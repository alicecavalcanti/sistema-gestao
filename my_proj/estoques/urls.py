

from django.urls import path
from . import views

urlpatterns = [
    path('', views.estoque_list, name='estoque_list'),
    path('view/<int:pk>', views.estoque_view, name='estoque_view'),
    path('new', views.estoque_create, name='estoque_new'),
    path('detail/<int:pk>', views.estoque_view, name='estoque_detail'),
    path('edit/<int:pk>', views.estoque_update, name='estoque_edit'),
    path('delete/<int:pk>', views.estoque_delete, name='estoque_delete'),
]
