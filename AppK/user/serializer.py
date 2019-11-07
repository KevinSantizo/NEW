from rest_framework import serializers
from django.contrib.auth import get_user_model
from user.models import Customer, Department, Town


User = get_user_model()


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
        user = User.objects.create_user(**validate_data)
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

