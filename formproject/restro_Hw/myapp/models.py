from django.db import models

# Create your models here.

class Restromenudb(models.Model):
    Item_Name=models.CharField(max_length=30)
    i_type=(('DRY','Dry'),('GRAVY','Gravy'))
    Item_Type=models.CharField(choices=i_type, max_length=5, blank=False, null=False)
    Image=models.ImageField(upload_to='Item_images')
