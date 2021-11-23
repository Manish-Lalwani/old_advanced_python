from crud_operation_app.viewsets import TempDataTableViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('TempDataTable',TempDataTableViewset)
