from django import forms 
from .models import Contatto
'''
class FormContatto(forms.Form):
    nome = forms.CharField()
    cognome = forms.CharField()
    email = forms.EmailField()
    contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder" : "Area Testuale! Scrivi pure!"}))
'''
# forms.Form → definisci manualmente i campi
# forms.ModelForm → i campi vengono generati automaticamente da un modello Django
class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto 
        fields = "__all__"#specifica tutti i campi