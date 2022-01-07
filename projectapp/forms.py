from django import forms
from django.db.models.fields import files
from django.db.models.fields.files import FileField
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import FileInput, TextInput
from . models import Wishlist, Purchase


class Customerform(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = "__all__"
        
        widgets = {
            'course': TextInput(attrs={
                
            })
        }
        
    
class ProjectPurchase(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['file']
        
        widgets = {
            'file':FileInput(attrs={
                'class':'form-control'
            })
        }