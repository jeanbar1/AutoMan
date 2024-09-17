from django import forms
from .models import Manutencao

class ManutencaoF(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['veiculo', 'oficina', 'tipoServico', 'data', 'custo']
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'oficina': forms.Select(attrs={'class': 'form-control'}),
            'tipoServico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de Serviço'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'custo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
        }
