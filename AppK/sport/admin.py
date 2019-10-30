from django.contrib import admin
from sport.models import Field, Company, Reservation, Schedule, Image


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'status', 'type', 'price')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('town', 'name', 'address', 'phone', 'email', 'image')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'company_reserve', 'customer_reserve', 'field_reserve', 'schedule_date')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('field', 'start_time', 'status')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('company', 'image')


