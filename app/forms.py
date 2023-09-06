from django import forms
from .models import User
from django.core import validators

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'number', 
            'firstname', 
            'lastname', 
            'birtday',
            'language',
            'country'
            ]
        widgets = {
            'number': forms.NumberInput(attrs={'class':'form-control'}),
            'firstname': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'birtday': forms.DateInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }