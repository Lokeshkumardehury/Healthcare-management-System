from django.contrib import admin
from django.urls import path
from .views import aviewdata,ahome,update
urlpatterns = [
    path('aviewdata',aviewdata,name='aviewdata'),
    path('update',update,name='update'),
    #myadmin
    path('ahome',ahome,name='ahome'),
]
