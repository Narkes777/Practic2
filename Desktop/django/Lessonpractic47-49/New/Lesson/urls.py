from . import views
from django.urls import path

urlpatterns = [
    path('cars/', views.CarList.as_view(), name='car_list'),
    path('cars/<int:pk>', views.CarDetail.as_view(), name='car_detail'),
    path('cars/create', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car_delete'), 

    path('categorys/', views.CategoryList.as_view(), name='category_list'),
    path('categorys/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('categorys/create', views.CategoryCreate.as_view(), name='category_create'),
    path('categorys/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('categorys/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),  
]