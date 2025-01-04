from django.contrib import admin
from django.urls import path
from doctor.views import dhome,dview,dprofile
urlpatterns = [
    #doctor
    path('dhome',dhome,name='dhome'),
    path('dview',dview,name='dview'),
    path('dprofile',dprofile,name='dprofile'),
    
]
