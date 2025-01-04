from django.contrib import admin
from django.urls import path
from contact.views import contacts,cviewdata,update
urlpatterns = [
    #contact
    path('',contacts),
    path('cviewdata',cviewdata,name='cviewdata'),
    path('update',update,name='update'),
]
