"""LostandFoundPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from lostandfoundapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #website
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('1', views.oldest, name='oldest'),
    path('create/', views.create, name='create'),
    path('delete/<int:post_pk>/', views.delete, name='delete'),
    path('viewpost/<int:post_pk>/', views.viewpost, name='viewpost'),
    path('myposts/', views.myposts, name='myposts'),


    #authentication
    path('signup/', views.signupsystem, name='signupsystem'),
    path('login/', views.loginsystem, name='loginsystem'),
    path('logout/', views.logoutsystem, name='logoutsystem'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
