from django.urls import path
from .views import MenuItemsByCategoryView

urlpatterns = [
    path('items-by-category/',MenuItemsByCategoryView.as_view(), name = 'items-by')
]