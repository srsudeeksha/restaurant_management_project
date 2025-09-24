from rest_framework.generics import ListAPIView
from .models import MenuItem
from .serializers import MenuItemSerializer

class DailySpecialsView(ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        return MenuItem.Objects.filter(is_daily_special=True)
        