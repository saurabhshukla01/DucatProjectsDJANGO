from rest_framework.serializers import ModelSerializer
from .models import *

class UserCreateSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = [
        'name',
        'house_name',
        'email',
        'password',
    ]  