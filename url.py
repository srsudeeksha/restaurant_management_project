from django.urls import path
from . import views

urlpatterns = [
    path('', views.todays_specials, name='todays_specials'),
]