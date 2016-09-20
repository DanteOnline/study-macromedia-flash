from django import forms

class ProfiForm(forms.Form):
    answer = forms.CharField(max_length=100, label='Ответ', widget=forms.TextInput(attrs={'class':'form-control'}))
