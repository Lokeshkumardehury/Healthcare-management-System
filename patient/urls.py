from django.contrib import admin
from django.urls import path
from patient.views import phome,pview
urlpatterns = [
    
    #patient
    path('phome',phome,name='phome'),
    path('pview',pview,name='pview'),
]
