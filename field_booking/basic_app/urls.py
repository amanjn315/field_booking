from django.contrib import admin
from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.index, name="index"),
    path('register/',views.register, name = 'register'),
    path('contact/',views.contact,name = "contact"),
    path('apeo_login/',views.apeo_login,name = "apeo_login"),
    path('details/',views.details,name = "details"),
    path('user_login/',views.user_login,name= 'user_login'),
]
