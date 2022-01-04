from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('signin',views.signIn,name="signin"),

    path('login',views.login,name="login"),

    path('logout',views.logout,name="logout")# webpage usmein hum shortcut derehe hy front end(name="logout")
    
]
