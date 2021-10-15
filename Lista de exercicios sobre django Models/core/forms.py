from django import forms
from core.models import People


class InserePessoaForm(forms.ModelForm):

    class Meta:
        model = People
        fields = "__all__"
