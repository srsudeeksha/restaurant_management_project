from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.submit_feedback,name='submit_feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success')
]