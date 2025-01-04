from django.shortcuts import render
from signup.models import signup_master

# Create your views here.
def phome(request):
    name=request.session.get('name')
    return render(request,'phome.html',{'name':name})
def pview(request):
    name=request.session.get('name')
    ob=signup_master.objects.filter(name=name)
    return render(request,'pview.html',{'data':ob})
    