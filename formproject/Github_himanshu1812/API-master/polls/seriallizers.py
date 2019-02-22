from rest_framework import serializers
from .models import *

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','name','age')