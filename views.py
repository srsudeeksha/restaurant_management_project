from rest_framework.viewss import APIView
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantInfoView(APIView):
    def get(self, request):
        restaurant = Restaurant.objects.first()
        if restaurant is None:
            return Response({'error':'No restaurant found.'}, status = 404)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)