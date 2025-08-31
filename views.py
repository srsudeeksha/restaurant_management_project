def home(request):
    menu_items=[
        {"name":"Margherita Pizza","price":250},
        {"name":"Veg Burger","price":150},
        {"name":"French Fries","price":100},
        {"name":"Chocolate Milkshake","price":180},
        {"name":"Pasta Alfredo","price":220},
    ]

    query = request.GET.get("q")
    if query:
        menu_item = [item for item in menu_item if query.lower()in item["name"].lower()]

    return render(request,"home.html",{"menu_items":menu_items,"query":query})