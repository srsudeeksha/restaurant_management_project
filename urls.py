from django.urls import path
from .views import OrderHistoryView

urlpatteerns = [
    path('history/',OrderHistoryView.as_view(),name='order-history'),
]