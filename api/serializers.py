from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Product

class SignupSerializers(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, min_length=8, max_length=64)


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']

        )

        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',]

        read_only_fields = ('id',)