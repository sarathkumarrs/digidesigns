from django import forms
from django.forms import TextInput, EmailInput

from users.models import Customer


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Customer
        exclude = ['user']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'password': TextInput(attrs={'class': 'form-control'}),
        }
