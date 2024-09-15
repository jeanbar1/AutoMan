from django import forms
from .models import Oficina


class OficinaF(forms.ModelForm):

    class Meta:
        model = Oficina
        fields = ['nome', 'endereco', 'telefone', 'especialidade']

        def __init__(self, *args, **kwargs):
            super(OficinaF, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control'})