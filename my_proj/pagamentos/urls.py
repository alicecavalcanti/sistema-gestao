from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagamento_list, name='pagamento_list'),
    path('view/<int:pk>/', views.pagamento_view, name='pagamento_view'),
    path('new/', views.pagamento_create, name='pagamento_new'),
    path('edit/<int:pk>/', views.pagamento_update, name='pagamento_edit'),
    path('delete/<int:pk>/', views.pagamento_delete, name='pagamento_delete'),
]
