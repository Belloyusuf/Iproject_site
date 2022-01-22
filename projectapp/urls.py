
from django.urls import path
from . import views


urlpatterns = [
    path('project/', views.project_list, name='project_list'),
    path('<slug:category_slug>/', views.project_list, name='project_list_by_category'),
    path('<int:id>/<slug:slug>/', views.project_detail, name='project_detail'),
    path('search', views.search, name='search'),

]
