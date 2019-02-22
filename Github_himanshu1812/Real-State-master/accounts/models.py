from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    is_seller = models.BooleanField('seller status', default=False)
    description = models.TextField(blank=True)
    register_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    photo = models.ImageField(upload_to='user', default='default.png', null=True, blank=True)



