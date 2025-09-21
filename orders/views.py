from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as drf_status
from .models import Order

class CancelOrderAPIView(APIView):
    def delete(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            if order.customer != request.user:
                return Response({'error':'You can only cancel your own orders.'}, status = drf_status.HTTP_403_FORBIDDEN)
            order.status = 'Cancelled'
            order.save()
            return Response({'status':'Order cancelled.'}, status=drf_status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({'error':'Order not found.'}, status=drf_status.HTTP_404_NOT_FOUND)
            