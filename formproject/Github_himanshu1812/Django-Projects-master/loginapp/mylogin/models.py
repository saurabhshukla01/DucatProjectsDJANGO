from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,blank=True,null=True)
    #post=models.ForeignKey(comment,blank=True,null=True)
    
    content=models.TextField()
    date_created=models.DateTimeField(auto_now=True,blank=True,null=True)
    pic=models.FileField(upload_to='images',blank=True,null=True)
    
    def __unicode__(self):
        return self.content

    class Meta:
        ordering=['-date_created']

   
class comment(models.Model):
    post=models.ForeignKey(Post,blank=True,null=True)
    cmt_user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    user_comment=models.CharField(max_length=255,blank=True,null=True)
    date=models.DateTimeField(auto_now=True,blank=True,null=True)

    def __unicode__(self):
        return self.user_comment

class Profile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=50,null=True,blank=True)
    job_title = models.CharField(max_length=50,null=True,blank=True)
    pic = models.FileField(upload_to='images',blank=True,null=True)

    class Meta:
        db_table = 'auth_profile'
        
    def __unicode__(self):
        return self.location

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
