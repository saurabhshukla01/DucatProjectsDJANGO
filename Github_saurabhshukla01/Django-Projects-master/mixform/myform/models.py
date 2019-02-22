from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User)
    location = models.CharField(max_length=100)
    job_title= models.CharField(max_length=100)

    def __unicode__(self):
        return self.location
