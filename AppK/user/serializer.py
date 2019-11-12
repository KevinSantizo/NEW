from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import Customer, Department, Town
from django.contrib.auth.hashers import make_password




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 2

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class TownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'
        depth = 1


class DoCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DoTownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'
        detph = 1


class CreateUserSerializer(serializers.ModelSerializer):
    def create (self, validate_data):
        hashed_pwd = make_password(validate_data)
        user = User.objects.create(**validate_data)
        user.password = hashed_pwd
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

