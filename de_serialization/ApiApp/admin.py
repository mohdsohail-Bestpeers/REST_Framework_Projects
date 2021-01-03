from django.contrib import admin
from .models import student
# Register your models here.

class stuAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']

admin.site.register(student,stuAdmin)