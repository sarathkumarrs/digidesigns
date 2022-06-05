from django import forms
from django.forms import TextInput

from diagrams.models import Module, Process, Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['creator']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'})
        }


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        exclude = ['project']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'})
        }


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        exclude = ['module']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'})
        }
