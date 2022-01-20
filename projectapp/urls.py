
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from account import views as  as_views



urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<slug:category_slug>/', views.project_list, name='project_list_by_category'),
    path('<int:id>/<slug:slug>/', views.project_detail, name='project_detail'),
    path('search', views.search, name='search'),
    path('register/', as_views.register, name='register')

]
