# Generated by Django 5.1.1 on 2024-09-16 03:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oficina', '0001_initial'),
        ('veiculo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('tipoServico', models.CharField(max_length=100)),
                ('custo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.oficina')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculo.veiculo')),
            ],
        ),
    ]
