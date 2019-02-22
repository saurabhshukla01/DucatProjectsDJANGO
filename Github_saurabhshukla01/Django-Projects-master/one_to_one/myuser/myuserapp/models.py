from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Emp(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField(max_length=20)

    def __unicode__(self):
        return self.department
