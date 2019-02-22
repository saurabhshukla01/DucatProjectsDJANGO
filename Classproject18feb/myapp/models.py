from django.db import models
from django.urls import reverse

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=10,null=True,blank=True)
    image = models.ImageField(upload_to="Restaurant")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')    

class Dish(models.Model):
    restaurant_name = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=30)
    dish_price = models.IntegerField()
    dish_image = models.ImageField(upload_to="Dish")  

    def __str__(self):
        return self.dish_name  

    def get_absolute_url(self):
        return reverse('home') 