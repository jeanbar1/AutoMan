from django.urls import path
from .views import user_login, user_logout, useradd
from . import views

urlpatterns = [
    path('addUser/', useradd, name='addUser'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='userlogout' ), 
    path('edit/<int:usuario_id>/', views.editar, name='user_edit'),
    path('perfil/<int:usuario_id>/', views.perfil, name='user_detail'),
    path('delete/<int:id>', views.excluirP, name='user_delete'),
]
