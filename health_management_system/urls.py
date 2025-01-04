"""
URL configuration for health_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from home import views as hviews
from signup.views import signup

from login.views import signin
from change_profile.views import profile_page

urlpatterns = [
     path('myadmin/', include('myadmin.urls')),
     path('patient/', include('patient.urls')),
     path('doctor/', include('doctor.urls')),
     path('contacts/', include('contact.urls')),
    
    path('admin/', admin.site.urls),

    #signup
    path('signup/',signup),

    #login
    path('signin/',signin),
    #profile
    path('profile_page',profile_page,name='profile_page'),
    

    #home
    path('home/', hviews.home),
    path('', hviews.index),
    path('about/', hviews.about),
    path('contact/', hviews.contact),
    path('register/', hviews.register),
    path('gallery/', hviews.gallery),
    path('faq/', hviews.faq),
    path('login/', hviews.login),
    path('course/<courseid>', hviews.coursedetails),
]

