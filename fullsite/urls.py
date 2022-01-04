from django.contrib import admin  #for admin panel keliye
from django.urls import path,include
from . import views


urlpatterns = [

    path('home',views.home,name="home"),

    path('about',views.about,name="about"),

    path('contact',views.contact,name="contactus"),

    path('order',views.addAddress,name="order"),

    path('tracker',views.trackeringsatus,name="trackingstatus"),

    path('search',views.search,name="search"),

    path('productview',views.productview,name="productview"),

    path('payment_complete/<str:userPk>',views.payment_complete,name="payment_complete"),#thorgh which we are send the data to reaspay
    
    path('payment',views.payment,name="payment"),
     
    path('cart',views.cart,name="cart"),


    path('gateway',views.gateway,name='gateway')

]