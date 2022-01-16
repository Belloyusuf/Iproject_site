from django import forms
from django.forms.widgets import EmailInput, FileInput, PasswordInput, Select, SelectMultiple, TextInput, Textarea

# User login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=6, required=True)
    
    widgets = {
        'username': TextInput(attrs={
            'class':'form-control',
            'placeholder':'John Smith'
        }),
        'password':PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'******'
        })
    }
