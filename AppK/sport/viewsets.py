from rest_framework import viewsets
from rest_framework import routers
from sport.models import Reservation, Field, Company, Schedule, Implement
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
    FieldChildSerializer,
    ImplementSerializer,
    CountScheduleSerializer
    )


class ReservationViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class FieldViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DoReservationViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Reservation.objects.all()
    serializer_class = DoReservationSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class CompanyFieldViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Company.objects.all()
    serializer_class = CompanyFieldSerializer


class CompanyDetailViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer


class DepartmentChildViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Department.objects.all()
    serializer_class = DepartmentChildSerializer


class TownChildViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Town.objects.all()
    serializer_class = TownChildSerializer


class DoScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Schedule.objects.all()
    serializer_class = DoScheduleSerializer


class FieldChildViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Field.objects.all()
    serializer_class = FieldChildSerializer


class ImplementViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Implement.objects.all()
    serializer_class = ImplementSerializer


class CountScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Schedule.objects.filter(status__exact='2')
    serializer_class = CountScheduleSerializer