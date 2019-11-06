from rest_framework import routers
from sport.viewsets import ( 
     ReservationViewSet, 
     FieldViewSet, 
     CompanyViewSet, 
     DoReservationViewSet, 
     ScheduleViewSet, 
     CompanyDetailViewSet, 
     CompanyFieldViewSet, 
     DepartmentChildViewSet, 
     TownChildViewSet,
     DoScheduleViewSet,
     FieldChildViewSet,
     ImplementViewSet,
     CountScheduleViewSet
)
from sport import views
from django.urls import path


router = routers.SimpleRouter()
router.register('reservations', ReservationViewSet)
router.register('do-reservation', DoReservationViewSet)
router.register('fields', FieldViewSet)
router.register('companies', CompanyViewSet)
router.register('schedules', ScheduleViewSet)
router.register('field-company', CompanyFieldViewSet)
router.register('detail-company', CompanyDetailViewSet)
router.register('department-child', DepartmentChildViewSet)
router.register('town-company', TownChildViewSet)
router.register('do-schedule', DoScheduleViewSet)
router.register('field-schedule', FieldChildViewSet)
router.register('implements', ImplementViewSet)
router.register('count', CountScheduleViewSet)

urlpatterns = router.urls