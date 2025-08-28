from django.urls import path
form . import views

urlpatterns = [
    path('contact/',views.contact_views, name='contact'),
    path('thank-you/',views.contact_view, name='thank_you'),
]