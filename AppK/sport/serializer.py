from rest_framework import serializers
from sport.models import Field, Reservation, Company, Schedule


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
        fields = ('name', 'address', 'phone', 'email', 'image', 'field_set')
        read_only_fields = ('name', 'field_set')

class DoReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'