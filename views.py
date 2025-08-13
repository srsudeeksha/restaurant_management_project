from datetime import datetime

def home(request):
    context = {
        'restaurant_name': 'Nothing Before Milkshake',
        'welcome_message': 'Welcome to our milkshake paradise!',
        'current_year': datetime.now().year
    }
    return render(request, 'home.html', context)

def reservations(request):
    context = {
        'current_year'
    }