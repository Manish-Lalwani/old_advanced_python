from rest_framework import viewsets
from . import models
from . import serializer

class TempDataTableViewset(viewsets.ModelViewSet):
    queryset = models.TestDataTable.objects.all()
    serializer_class = serializer.TestDataTableSerializer
