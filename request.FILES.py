def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MenuItemForm()