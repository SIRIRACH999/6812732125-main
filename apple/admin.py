from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("studentID", "prefix", "Firstname", "Lastname", "runnumber")
    search_fields = ("studentID", "Firstname", "Lastname", "prefix")
    list_filter = ("runnumber",)