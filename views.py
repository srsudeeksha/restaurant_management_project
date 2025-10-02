from rest_framework import generics
from .models import Table
from .serializers import TableSerializers

class TableSerializersAPIView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer