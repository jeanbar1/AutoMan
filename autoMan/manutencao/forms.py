from django import forms
from .models import Manutencao


class ManutencaoF(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = ['veiculo', 'tipoServico', 'data_manutencao', 'preco']
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'tipoServico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tipoServico'}),
            'data_manutencao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'preco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
        }

        