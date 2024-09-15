from django.db import models


class Manutencao(models.Model):
    veiculo = models.ForeignKey('veiculo.Veiculo', on_delete=models.CASCADE)
    oficina = models.ForeignKey('oficina.Oficina', on_delete=models.CASCADE)
    data = models.DateField()
    tipoServico = models.CharField(max_length=100)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
