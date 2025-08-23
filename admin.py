from django.contrib import admin
from .models import Menu, Order

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name","price","description")
    search_fields = ("name",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=("id","Customer_name","menu_item","quantity","created_at")
    list_filter=("created_at",)
    search_fields=("customer_name",)