from rest_framework import viewsets
from user.models import Customer, Department, Town
from user.serializer import CustomerSerializer, DepartmentSerializer, TownSerializer, DoCustomerSerializer, DoTownSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class TownViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class DoCustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = DoCustomerSerializer


class DoTownViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = DoTownSerializer

    