from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from leaflet.admin import LeafletGeoAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Cloud

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cloud, LeafletGeoAdmin)


