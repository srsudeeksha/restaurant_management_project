from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReviewSerializer

class ReviewCreateView(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serialier.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        