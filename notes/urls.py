from django.urls import path
from . import views

app_name='notes'

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('home/',views.home_page,name='home_page'),
    path('update/',views.update,name='update'),
    path('register/',views.register,name='register'),
    path('settings/',views.settings,name='settings'),
    

]