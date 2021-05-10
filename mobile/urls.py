"""Mobileproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from .views import index_page,list_mobile,user_register,user_login,index_page2,create_product,mobile_detail,product_details\
    ,update_mobile,delete_mobile,product_view,user_logout,order_product,add_to_cart,my_cart,remove_order,account_details,\
    view_orders,cancel_order
urlpatterns = [
    path("",index_page,name="index"),
    path("listmobile",list_mobile,name="list"),
    path('register',user_register,name="user_register"),
    path('login',user_login,name="user_login"),
    path("homepage",index_page2,name="user_home"),
    path("addproduct",create_product,name="add_product"),
    path("mobileview/<int:id>",mobile_detail,name="mobile_view"),
    path("productdetails",product_details,name="product_detail"),
    path("updatemobile/<int:id>",update_mobile,name="update_mobile"),
    path("deletemobile/<int:id>",delete_mobile,name="delete_mobile"),
    path("productview/<int:id>",product_view,name="product_view"),
    path("userlogout",user_logout,name="user_logout"),
    path("orderproduct/<int:id>",order_product,name="order_product"),
    path("cartadd/<int:id>",add_to_cart,name="add_cart"),
    path("mycart",my_cart,name="my_cart"),
    path("deleteorder/<int:id>",remove_order,name="remove"),
    path("accounts",account_details,name="ac"),
    path("vieworders",view_orders,name="view_order"),
    path("ordercancelled/<int:id>",cancel_order,name="cancel"),


]
