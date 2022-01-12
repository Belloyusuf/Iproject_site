from django import forms
from django.db.models.fields import files
from django.db.models.fields.files import FileField
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import EmailInput, FileInput, Select, SelectMultiple, TextInput, Textarea
from . models import Wishlist, Purchase, Comment



class SharebyEmail(forms.Form):
    """ Form that would handle sharing of projects via email """
    name = forms.CharField( max_length=50, required=True)
    email = forms.EmailField(required=True)
    to = forms.EmailField(required=True)
    comments = forms.CharField(widget=forms.Textarea,required=False)


class Customerform(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = "__all__"
        
        widgets = {
            'course': TextInput(attrs={
                'class':'form-control',
                'placeholder':'E.g, C-programming'
            }),
            'topic': TextInput(attrs={
                'class':'form-control',
                'placeholder':'E.g, Student Management System'
            }),
             'description': Textarea(attrs={
                'rows':3, 
                'class':'form-control',
                
            }),
              'email': EmailInput(attrs={
                'class':'form-control',
                'placeholder':'John@gmail.com'
            })
        }
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'project')
        widgets = {
            'name':TextInput(attrs={
                'class':'form-control',
                'placeholder':'John Smith'
            }),
            'email':EmailInput(attrs={
                'class':'form-control',
                'placeholder':'anything@gmail.com'
            }),
            'project':Select(attrs={
                'classs':'form-control',
                'placeholder':'choose project'
            }),
            'body':Textarea(attrs={
                'rows':3,
                'class':'form-control'
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