from django.urls import path
from . import views


# app_name = 'app'


urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<slug:category_slug>/', views.project_list, name='project_list_by_category'),
    path('<int:id>/<slug:slug>/', views.project_detail, name='project_detail'),
    path('search', views.search, name='search'),
    path('UserGuid_detail/', views.UserGuid_detail, name='UserGuid_detail'),
    path('wishlist/', views.user_wishlist, name='wishlist'),
    path("purchase/", views.PurchaseCreateView.as_view(), name="purchase"),
]
