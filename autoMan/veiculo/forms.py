from django import forms
from .models import Veiculo

class VeiculoF(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'ano', 'cor', 'proprietario', 'placa']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
            'ano': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ano'}),
            'cor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cor'}),
            'proprietario': forms.Select(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Placa'}),
        }
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['marca'].label = 'Marca'
        self.fields['modelo'].label = 'Modelo'
        self.fields['ano'].label = 'Ano'
        self.fields['cor'].label = 'Cor'
        self.fields['proprietario'].label = 'Proprietário'
        self.fields['placa'].label = 'Placa'

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})