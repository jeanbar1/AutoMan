from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nome = models.CharField(max_length= 100)
    cpf = models.CharField(max_length= 11, unique=True)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=500)

    def __str__(self):
        return self.nome
    