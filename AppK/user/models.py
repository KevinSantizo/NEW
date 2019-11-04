from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        

class Town(models.Model):
    department = models.ForeignKey(Department, related_name='towns', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ', ' + self.department.name


class Customer(models.Model):
    town = models.ForeignKey(Town, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.first_name + '  ' + self.last_name