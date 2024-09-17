from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.oficinaListar, name='oficinaListar'),
    path('add/', views.oficinaAdd, name='oficinaAdd'),
    path('editar/<int:id>/', views.oficinaEditar, name='oficinaEditar'),
    path('detalhe/<int:id>/', views.oficinaDetalhe, name='oficinaDetalhe'), 
    path('excluir/<int:id>/', views.oficinaDeletar, name='oficinaDeletar'),
]
