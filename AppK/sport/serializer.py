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


class CompanyFieldSerializer(serializers.ModelSerializer):
    field_set = FieldSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ('town', 'id', 'name', 'address', 'phone', 'email', 'image', 'field_set')
        read_only_fields = ('name', 'field_set')
        depth = 2
        

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
    town_set = DoTownSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ('name', 'town_set')
        read_only_fields = ('name', 'town_set')


class TownChildSerializer(serializers.ModelSerializer):
    company_set = CompanySerializer(many=True, read_only=True)
    class Meta:
        model = Town
        fields = ('name', 'company_set')
        read_only_fields = ('name', 'company_set')


class DoScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class FieldChildSerializer(serializers.ModelSerializer):
    schedule_set = DoScheduleSerializer(many=True, read_only=True)
    class Meta:
        model = Field
        fields = ( 'id', 'name', 'status', 'type', 'price', 'schedule_set')
        read_only_fields = ('id', 'name', 'status', 'type', 'price', 'schedule_set')
        
        
