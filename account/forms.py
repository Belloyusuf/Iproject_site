from django import forms
from django.forms.widgets import EmailInput, FileInput, PasswordInput, Select, SelectMultiple, TextInput, Textarea
from django.contrib.auth.models import User



# User Registration form
class UserRegistrationForm(forms.ModelForm):
    """ User Registration form """
    password = forms.CharField(max_length=6, required=True, 
                               widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=6, required=True,
                                widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'image')
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password did\'t match')
        return cd['password2']


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
