from django import forms
from .models import Transacao

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ('descricao', 'valor', 'data_transacao', 'recorrencia', 'pago', 'tipo_transacao')