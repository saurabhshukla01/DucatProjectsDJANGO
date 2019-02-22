from django.db import models



# Create your models here.
class AddharForm(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    DOB = models.DateField()
    Gender = models.CharField(max_length=10)
    Address = models.CharField(max_length=30)
    Parents_name = models.CharField(max_length=20)
    Mob_no = models.CharField(max_length=10,null=True,blank=True)