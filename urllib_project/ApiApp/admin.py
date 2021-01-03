from django.contrib import admin
from .models import Student
# Register your models here.




class stuAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll']


admin.site.register(Student,stuAdmin)
