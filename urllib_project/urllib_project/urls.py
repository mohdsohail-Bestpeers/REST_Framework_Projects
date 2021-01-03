"""urllib_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ApiApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student),
    path('list/', views.studentapi.as_view()),
    path('form/',views.student_form),
    path('formapi/',views.studentformapi.as_view()),
    path('update/<id>/',views.student_update, name='update'),
    path('updateapi/<pk>/',views.studentUpdate.as_view()),
    path('delete/<id>/',views.student_delete, name='delete'),
    path('deleteapi/<pk>/',views.studentDelete.as_view()),

    
]
