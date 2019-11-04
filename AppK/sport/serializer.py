from rest_framework import serializers
from sport.models import Field, Reservation, Company, Schedule
from user.models import Department, Town
from user.serializer import DepartmentSerializer, DoTownSerializer


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        depth = 1


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DoReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        depth = 3


class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        depth = 2


class DepartmentChildSerializer(serializers.ModelSerializer):
    towns = DoTownSerializer(many=True)
    class Meta:
        model = Department
        fields = ('id', 'name', 'description', 'towns')


class TownChildSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(many=True)
    class Meta:
        model = Town
        fields = ('id', 'name', 'companies') 


class DoScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class FieldChildSerializer(serializers.ModelSerializer):
    schedules = DoScheduleSerializer(many=True)
    class Meta:
        model = Field
        fields = ( 'id', 'name', 'status', 'type', 'price', 'schedules')
        
        

class CompanyFieldSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)
    class Meta:
        model = Company
        fields = ('town', 'id', 'name', 'address', 'phone', 'email', 'image', 'fields')
        depth = 4
