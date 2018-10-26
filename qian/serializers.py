from rest_framework import serializers
from qian.models import user,data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields=["username","email","lijie","time",]

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = data
        fields=["user","name","fk","url","cookie","header","data",]
