from django.contrib import admin
from user.models import Customer, Department, Town
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'address', 'password')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ('department', 'name')