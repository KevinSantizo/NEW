from rest_framework import viewsets
from rest_framework import routers
from sport.models import Reservation, Field, Company, Schedule
from user.models import Department, Town
from sport.serializer import (
    ReservationSerializer, 
    DepartmentChildSerializer, 
    FieldSerializer,
    CompanySerializer, 
    DoReservationSerializer, 
    ScheduleSerializer, 
    CompanyFieldSerializer,
    CompanyDetailSerializer, 
    TownChildSerializer,
    DoScheduleSerializer,
    FieldChildSerializer
    )


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


class CompanyDetailViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer


class DepartmentChildViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentChildSerializer


class TownChildViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = TownChildSerializer


class DoScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = DoScheduleSerializer


class FieldChildViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldChildSerializer

