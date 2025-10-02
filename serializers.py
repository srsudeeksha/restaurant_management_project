from rest_framework import serializers
from .models import Table

class TableSerializers(serializers.ModelSerializer):
    class Meta:
        model = Table 
        fields = ['table_number', 'capacity','is_available']
        