from django.contrib import admin
from .models import Userprofile

@admin.register(Userprofile)
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ("user","phone_number")