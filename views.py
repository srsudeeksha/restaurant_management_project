from django.shortcuts import render
from .models import Restaurant
def home(request):
    restaurant = Restaurant.objects.first()
    return render(request,'home.html',{'restaurant',restaurant})