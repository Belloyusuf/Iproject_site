from django.contrib import admin
from . models import Category, Project, ProjectDetail



admin.site.site_header = "C-Tech Company Limited"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
  
  
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'slug', 'updated', 'created']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug':('name',)}
    
    
@admin.register(ProjectDetail)
class ProjectDetailAdmin(admin.ModelAdmin):
    list_display = ['introduction', 'intro_desc', 'current', 'current_desc', 
                    'problem', 'problem_desc', 'proposed', 'prop_desc', 'objectives', 'obj_desc']
    
