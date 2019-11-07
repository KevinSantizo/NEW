from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from user.models import Customer, Department, Town
from user.serializer import (
    CustomerSerializer, 
    CreateUserSerializer, 
    DepartmentSerializer, 
    TownSerializer, 
    DoCustomerSerializer, 
    DoTownSerializer
)
User = get_user_model()


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class TownViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class DoCustomerViewSet(viewsets.ModelViewSet):
    permission_classes = []
    authentication_classes = []
    queryset = Customer.objects.all()
    serializer_class = DoCustomerSerializer


class DoTownViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = DoTownSerializer

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)  
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            return Response('success')
        else:
            return Response(serializer.errors)