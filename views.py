from django.shortcuts import render 
from django.http import HttpResponse
from datetime import datetime

def home(request):
    try:
        context = {
            'restaurant_name': 'Nothing Before Milkshake',
            'welcome_message': 'Welcome to our milkshake paradise!',
            'current_year': datetime.now().year
        }
        return render(request, 'home.html', context)
    except Exception as e:
        return HttpResponse(f"An error occured: {str(e)}", status = 500)   