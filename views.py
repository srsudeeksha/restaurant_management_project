from django.views.generic import ListView
from .models import MenuItem

class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu_list.html'
    context_object_name = 'menu_items'
    paginate_by = 10 