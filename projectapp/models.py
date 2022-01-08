from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250, unique=True)
    
    class Meta:
        ordering = ('-name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    # Defining url
    def get_absolute_url(self):
        return reverse("project_list_by_category", args=[self.slug])
    


class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='projects')
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True)
    image = models.ImageField(upload_to='project_image', blank=True, null=True)
    file = models.FileField(upload_to='Projects/%Y/%m/%d', blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    
    class Meta:
        ordering = ('-name',)
        index_together = (('id', 'slug'),)
        
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("project_detail", args=[self.id, self.slug])
    
    
class Wishlist(models.Model):
    """ Customer wish list """
    course = models.CharField(("Course Name"), max_length=150)
    topic = models.CharField(("Project Topic"), max_length=50)
    description = models.TextField(('Project Description'))
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    school_name = models.CharField(("Name of your school"), max_length=100, blank=False, null=False)
    
    
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


class Purchase(models.Model):
    project = models.ForeignKey(Project, verbose_name=(""), on_delete=models.CASCADE)
    file = models.FileField(("Transaction invoice"),upload_to="purchase")