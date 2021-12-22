from django import forms

class MyForm(forms.Form):
    first_name = forms.CharField()
    middle_name = forms.CharField()
    last_name = forms.CharField()
    full_name = forms.CharField()