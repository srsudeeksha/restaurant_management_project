from django.urls import path
from .views import MenuItemUpdateView

urlpatterns = [
    path('menu-items/<int:pk>/',MenuItemUpdateView.as_view(),name-'menu-item-update'),
]