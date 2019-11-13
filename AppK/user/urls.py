from rest_framework import routers
from user.viewsets import CustomerViewSet, DepartmentViewSet, TownViewSet, DoCustomerViewSet, DoTownViewSet, UserCeateViewSet
from user import views
from django.urls import path


router = routers.SimpleRouter()
router.register('customers', CustomerViewSet)
router.register('departments', DepartmentViewSet)
router.register('towns', TownViewSet)
router.register('do-customer', DoCustomerViewSet)
router.register('do-town', DoTownViewSet)
router.register('do-custo', UserCeateViewSet)

urlpatterns = router.urls