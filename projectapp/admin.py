from django.contrib import admin
from . models import Category, Project, Wishlist, Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'company']
    list_filter = ['title', 'company']

# @admin.register(Wishlist)
# class WishlistAdmin(admin.ModelAdmin):
#     list_display = ['course', 'topic', 'created', 'school_name']
#     list_filter = ['course', 'school_name', 'created']

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
    
