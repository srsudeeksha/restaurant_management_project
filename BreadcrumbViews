from django.shortcuts import render

def home(request):
    breadcrumbs = [
        {"name": "Home", "url": "/"},
    ]
    return render(request, "home.html", {"breadcrumbs": breadcrumbs})

def menu(request):
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name": "Menu", "url": "/menu/"},
    ]
    return render(request, "menu.html", {"breadcrumbs": breadcrumbs})

def order_confirmation(request):
    breadcrumbs = [
        {"name": "Home", "url": "/"},
        {"name": "Orders", "url": "/orders/"},
        {"name": "Confirmation", "url": "#"},
    ]
    return render(request, "order_confirmation.html", {"breadcrumbs": breadcrumbs})
