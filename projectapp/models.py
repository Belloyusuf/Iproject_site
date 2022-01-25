from distutils import text_file
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid

# Category class
class Category(models.Model):
    """ Category class """
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
    
    

# Project Description 
class ProjectDetail(models.Model):
    """ Project discription of each topic """
    # name = models.ForeignKey(Project, 
                            #  verbose_name=(""), on_delete=models.CASCADE)
    table_img = models.ImageField(("Table of content Image"), 
                                  upload_to='project_image', 
                                  height_field=None, 
                                  width_field=None)
    introduction = models.CharField(max_length=100)
    intro_desc = models.TextField(("Introduction Description"))
    
    current = models.CharField(("Current System"), max_length=100)
    current_desc = models.TextField(("Current System Description"))
    
    proposed = models.CharField(("Proposed New System"), max_length=100)
    prop_desc= models.TextField(("Proposed Description"))
    
    problem = models.CharField(("Problems Of Current System"), max_length=100)
    problem_desc = models.TextField(("Problem of current system Description"))
    
    objectives = models.CharField(("Objectives"), max_length=100)
    obj_desc = models.TextField(("Objectives Description"))
    
    # def __str__(self):
    #     return self.name
    
    

# Projec class 
class Project(models.Model):
    """ Class that would create a project file """
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='projects')
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=250, db_index=True)
    image = models.ImageField(upload_to='project_image',
                              blank=True, null=True)
    file = models.FileField(upload_to='Projects/%Y/%m/%d', 
                            blank=False, null=False)
    description = models.OneToOneField(ProjectDetail,
                                       on_delete=models.CASCADE)
                                   
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(("Last price"), 
                                    max_digits=10, decimal_places=2)
    rating = models.IntegerField(("Project Ratings"), default=0)
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
    
 