from django.db import models


class Profile(models.Model):
    name=models.CharField(max_length=30)
    age = models.IntegerField()
# Create your models here.
