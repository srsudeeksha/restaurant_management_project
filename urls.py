from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.menu_list, name="menu")
    path("add-to-cart/<int:item_id>/", views.add_to_cart, name="add_to_cart")
    path("cart/", views.view_cart, name="view_cart"),
]