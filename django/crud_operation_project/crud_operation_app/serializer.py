from rest_framework import serializers
from .models import TestDataTable

class TestDataTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDataTable
        fields = '__all__'  # or if some fiels write in a tuple ('id','firstname',etc...)