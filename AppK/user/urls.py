from rest_framework import routers
from user.viewsets import CustomerViewSet, DepartmentViewSet, TownViewSet, DoCustomerViewSet, DoTownViewSet
from user import views
from django.urls import path


router = routers.SimpleRouter()
router.register('customers', CustomerViewSet)
router.register('departments', DepartmentViewSet)
router.register('towns', TownViewSet)
router.register('do-customer', DoCustomerViewSet)
router.register('do-town', DoTownViewSet)
urlpatterns = router.urls