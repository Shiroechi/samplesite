from django import forms

class MyForm(forms.Form):
    first_name = forms.CharField(label="firstname")
    middle_name = forms.CharField(label="middlename")
    last_name = forms.CharField(label="lastname")
    full_name = forms.CharField(label="fullname")