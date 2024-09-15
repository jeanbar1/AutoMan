from django.db import models
from django.contrib.auth.models import User




class Oficina(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=500)
    telefone = models.CharField(max_length=11)
    especialidade = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.modelo