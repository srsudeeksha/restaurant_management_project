from django.urls import path
from .views import UserProfileUpdateView

urlpatterns = [
    path('user/profile/update/',UserProfileUpdateView.as_view(), name='user-profile-update'),
]