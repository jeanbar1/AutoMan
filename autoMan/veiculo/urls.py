from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.veiculoAdd, name='veiculoAdd'),
    path('listar/', views.veiculoListar, name='veiculoListar'),
    path('editar/<int:id>/', views.veiculoEditar, name='veiculoEditar'),
    path('detalhe/<int:id>/', views.veiculoDetalhe, name='veiculoDetalhe'),
    path('excluir/<int:id>/', views.veiculoDeletar, name='veiculoDeletar'),
]
