from django.urls import path
from django.views.generic import TemplateView
from . import views 

urlpatterns = [
    #path('',TemplateView.as_view(template_name="myapp/index.html"),name="index"),
    path('home/', views.Sample.as_view(), name="home"),
    path('addrestaurant/', views.AddRestaurant.as_view(), name="addrestaurant"),
    path('updaterestaurant/<int:pk>/', views.UpdateRestaurant.as_view(), name="updaterestaurant"), 
    path('', views.ListRestaurant.as_view(), name="restaurantlist"), 
    path('restaurantdetail/<int:id>', views.RestaurantDetail.as_view(), name="restaurantdetail"),
    path('deletedish/<int:pk>', views.DeleteDish.as_view(), name="deleteview") 
]