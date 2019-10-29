from rest_framework import viewsets
from rest_framework import routers
from sport.models import Reservation, Field, Company, Schedule
from sport.serializer import ReservationSerializer, FieldSerializer, CompanySerializer, DoReservationSerializer, ScheduleSerializer, CompanyFieldSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DoReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = DoReservationSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class CompanyFieldViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyFieldSerializer