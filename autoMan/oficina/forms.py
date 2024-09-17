from django import forms
from .models import Oficina

class OficinaF(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = ['nome', 'endereco', 'telefone', 'especialidade']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Nome da Oficina', 'aria-label': 'Nome da Oficina', 'maxlength': '100', 'style': 'width: 100%;'
            }),
            'endereco': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Endereço da Oficina', 'aria-label': 'Endereço da Oficina', 'rows': 3, 'maxlength': '255', 'style': 'width: 100%;'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Telefone de Contato', 'aria-label': 'Telefone de Contato', 'pattern': '[0-9]{10,11}', 'maxlength': '11', 'style': 'width: 100%;'
            }),
            'especialidade': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Especialidade da Oficina', 'aria-label': 'Especialidade da Oficina', 'maxlength': '100', 'style': 'width: 100%;'
            }),
        }


        def __init__(self, *args, **kwargs):
            super(OficinaF, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control'})