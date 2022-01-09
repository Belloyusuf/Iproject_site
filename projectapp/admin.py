from django.contrib import admin
from . models import Category, Project, Wishlist, Plan, Comment




admin.site.site_header = "C-Tech Company Limited"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'project', 'created', 'active']
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'company']
    list_filter = ['title', 'company']

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['course', 'topic', 'created', 'username']
    list_filter = ['course', 'username', 'created']

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
    
