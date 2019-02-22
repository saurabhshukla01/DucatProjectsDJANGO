from django import forms
from .models import Restaurant, Dish

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"