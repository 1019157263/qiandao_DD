from rest_framework import serializers
from qian.models import user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields=["username","email","lijie","time",]
