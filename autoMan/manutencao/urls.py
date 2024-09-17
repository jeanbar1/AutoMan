from django.urls import path
from . import views

urlpatterns = [
    path('', views.manuListar, name='manuListar'),
    path('add/', views.manuadd, name='manuadd'),
    path('editar/<int:id>/', views.manuEditar, name='manuEditar'),
    path('detalhe/<int:id>/', views.manuDetalhe, name='manuDetalhe'),
    path('deletar/<int:id>/', views.manuDeletar, name='manuDeletar'),
]
