from django.contrib import admin
from .models import Wishlist, Plan, Comment, Purchase



@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['course', 'topic', 'email']
    list_filter = ['course', 'email']
    

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'company']
    list_filter = ['title', 'company']



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'project', 'created', 'active']
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_course', 'project_name', 'email', 'created', 'upload_image', 'paid')
    list_filter = ('created', 'paid', 'project_course')