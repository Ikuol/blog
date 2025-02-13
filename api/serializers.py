from django.contrib.auth.models import User
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName',
                  'email', 'password', 'created_at']
