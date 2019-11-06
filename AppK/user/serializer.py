from rest_framework import serializers
from user.models import Customer, Department, Town


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

