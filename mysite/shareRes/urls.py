from django.urls import path, include
from . import views

urlpatterns = [
    path('shareRes', views.index, name='shareRes'),
    path('restaurantDetail/', views.restaurantDetail, name='resDetailPage'),
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'),
    path('categoryCreate/', views.categoryCreate, name='cateCreatePage'),
    path('categoryCreate/create', views.Create_category, name='cateCreate'),
    path('categoryCreate/delete', views.Delete_category, name='cateDelete'),
]