from django.db import models
from django.contrib.auth.models import User

class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)  
    marca = models.CharField(max_length=100)   
    ano = models.IntegerField()
    placa = models.CharField(max_length=10)   
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    cor = models.CharField(max_length=50)      

    def __str__(self):
        return self.modelo
