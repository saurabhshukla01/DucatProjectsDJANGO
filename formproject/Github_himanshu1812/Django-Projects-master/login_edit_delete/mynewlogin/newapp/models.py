from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_by=models.ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True,auto_now=False,null=True)

    def __unicode__(self):
        return self.title

class SharePost(models.Model):
    user = models.ForeignKey(User,blank=True,null=True)
    post=models.ForeignKey(Post,blank=True,null=True)
    

class Profile(models.Model):
    user=models.OneToOneField(User)
    pic=models.FileField(upload_to='pic',null=True)

    
    
