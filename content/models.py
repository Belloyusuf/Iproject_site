import imp
from django.db import models
from projectapp.models import Project, Category


class Wishlist(models.Model):
    """ Customer wish list """
    course = models.CharField(("Course Name"), max_length=150)
    topic = models.CharField(("Project Topic"), max_length=50)
    description = models.TextField(('Project Description'))
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    email = models.EmailField(("Email"), max_length=254)
    
    
    def __str__(self):
        return self.topic
    
    class Meta:
        ordering = ('-created',)
    

class Plan(models.Model):
    """ For plan and pricing """
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    company = models.CharField(max_length=150)   
    
    class Meta:
        verbose_name = ("Plan")
        verbose_name_plural = ("Plans")

    def __str__(self):
        return self.title



class Comment(models.Model):
    project = models.ForeignKey(Project, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(("Username"),max_length=50)
    email = models.EmailField(("Your Email"), max_length=250)
    body = models.TextField(("Your comment"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return (f" Commented by {self.name} on {self.project}")
    
    
class Purchase(models.Model):
    project_course = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    upload_image = models.FileField(upload_to="purchase")
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.project_course}'
