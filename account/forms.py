from django import forms
from django.forms import widgets
from django.forms.widgets import EmailInput, FileInput, PasswordInput, Select, SelectMultiple, TextInput, Textarea
from django.contrib.auth.models import User



# User Registration form
class UserRegistrationForm(forms.ModelForm):
    """ User Registration form """
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password')
        
        widgets={
            'username':TextInput(attrs={
                'class':'form-control',
                'placeholder':'John Smith'
            }),
            'first_name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'John'
            }),
            'email':EmailInput(attrs={
                'class':'form-control',
                'placeholder':'example@gmail.com'
            }),
            'password':PasswordInput(attrs={
                'class':'form-control'
            }),
        }



# User login form
class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'password')
        
        widgets={
            'username': TextInput(attrs={
                'class':'form-control',
                'placeholder':'John Smith'
            }),
            'password':PasswordInput(attrs={
                'class':'form-control'
            })
        }
