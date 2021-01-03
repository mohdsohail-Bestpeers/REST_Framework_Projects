from django.contrib import admin
from .models import student


@admin.register(student)
class stuAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']