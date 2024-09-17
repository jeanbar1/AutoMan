from django.db import models
from oficina.models import Oficina
from veiculo.models import Veiculo
from django.contrib.auth.models import User 


class Manutencao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    data = models.DateField()
    tipoServico = models.CharField(max_length=100)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
