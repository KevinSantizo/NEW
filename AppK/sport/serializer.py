from rest_framework import serializers
from datetime import datetime, time
from sport.models import Field, Reservation, Company, Schedule, Implement
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
        depth = 5


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


class CountScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        depth = 4
        

class FieldChildSerializer(serializers.ModelSerializer):
    schedules = serializers.SerializerMethodField('get_schedules')
    counts = serializers.SerializerMethodField('count_schedules')

    def get_schedules(self, field):
        sch = Schedule.objects.filter(start_time__gte=datetime.now(), status__exact=2, field=field)
        serializer = DoScheduleSerializer(instance=sch, many=True)
        return serializer.data

    def count_schedules(self, field):
        sch = Schedule.objects.filter(start_time__gte=datetime.now(), field=field).count()
        return sch

    class Meta:
        model = Field
        fields = ( 'company', 'id', 'name', 'status', 'type', 'price', 'schedules', 'counts')
        depth = 3


class CountSerializer(serializers.ModelSerializer):
    schedules = serializers.SerializerMethodField('get_count')

    def get_count(self, field):
        sch = Schedule.objects.filter(field=field).count()
        return sch

    class Meta:
        model = Field
        fields = ( 'company', 'id', 'name', 'status', 'type', 'price', 'schedules')
        

class CompanyFieldSerializer(serializers.ModelSerializer):
    fields = FieldChildSerializer(many=True)
    class Meta:
        model = Company
        fields = ('town', 'id', 'name', 'address', 'phone', 'email', 'image', 'fields')
        depth = 2


class ImplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Implement
        fields = '__all__'


