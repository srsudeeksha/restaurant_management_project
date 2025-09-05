from django.urls import path
from . import views

urlpatterns = [
    path("order/confirmation/",views.order_confirmation,name="order_confirmation"),
]