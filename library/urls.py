"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from manager.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('listusers',listusers,name='listusers'),
    path('listbooks',listbooks,name='listbooks'),
    path('adminlogin',adminlogin,name='adminlogin'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    path('infostd/<int:id>',infostd,name='infostd'),
    path('search',search,name='search'),
    path('prof',prof,name='prof'),
    path('updatepass/<int:id>',updatepass,name='updatepass'),
    path('addbook',addbook,name='addbook'),
    path('updatestd/<int:id>',updatestd,name='updatestd'),
    path('deletestd/<int:id>',deletestd,name='deletestd'),
    path('addstd',addstd,name='addstd'),
    path('adminlogout',adminlogout,name='adminlogout'),
    path('stdlogin',stdlogin,name='stdlogin'),
    path('stdlogout',stdlogout,name='stdlogout'),
    path('bookborrow/<int:id>',bookborrow,name='bookborrow'),
    path('listborrow',listborrow,name='listborrow'),
    path('ret/<int:id>',ret,name='ret'),
    path('stdbooks',stdbooks,name='stdbooks'),
    path('regist',regist,name='regist'),
    path('stdprof',stdprof,name='stdprof'),
    path('updateprof<int:id>',updateprof,name='updateprof')
    

]
