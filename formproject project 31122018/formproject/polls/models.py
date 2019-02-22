from django.db import models
from django.urls import reverse

class Employee(models.Model):
    ename = models.CharField(max_length=30)
    eage = models.IntegerField()
    ecity = models.CharField(max_length=30)
    edsg = models.CharField(max_length=30)

    class Meta:
        db_table = 'emp'
		
    def get_absolute_url(self):
        return reverse('index')
# Create your models here.
