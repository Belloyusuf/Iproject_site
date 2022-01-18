from django import forms
from django.core.files import images
from django.db.models.fields import files
from django.db.models.fields.files import FileField, ImageField, ImageFieldFile
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import EmailInput, FileInput, PasswordInput, Select, SelectMultiple, TextInput, Textarea
from . models import Wishlist, Purchase, Comment




# Customer wish list form
class Customerform(forms.ModelForm):
    """ A form that allowed customer to send their wishlist project """
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
        
        
# Comment form
class CommentForm(forms.ModelForm):
    """ class that would create comment form to users """
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
                'class':'form-control',
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
        fields = ('__all__')
        
        widgets = {
            'project_course':Select(attrs={
                'class':'form-control',
                'placeholder':'Java programming'
            }),
            'project_name':Select(attrs={
                'class':'form-control',
                'placeholder':'Student Management Syste'
            }),
             'email':EmailInput(attrs={
                'class':'form-control',
                'placeholder':'anything@gmail.com'
            }),
             'upload_image':FileInput(attrs={
                 'class':'form-control',
             })
        }
        