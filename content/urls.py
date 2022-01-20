import imp
from django.urls import path
from . import views
from projectapp import views as project_views


app_name = 'site_content'

urlpatterns = [
    path('wishlist/', views.user_wishlist, name='wishlist'),
    path('UserGuid_detail/', views.UserGuid_detail, name='UserGuid_detail'),
    path('comment/', views.user_comment, name='comment'),
    path('purchase/', views.purchaseProject, name="purchase"),

]
