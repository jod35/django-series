from django.contrib import admin
from django.urls import path,include
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('notes.urls'),name='notes'),
]
