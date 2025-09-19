from django.urls import path
from .views import MenuItemSearchView

urlpatterns = [
    path('menu-item/search/', MenuItemSearchView.as_view(), name='menu-item-search'),
]