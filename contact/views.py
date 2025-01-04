from django.shortcuts import render,redirect
from .models import contact_master
# Create your views here.
def contacts(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        address=request.POST['address']
        ob=contact_master.objects.create(name=name,email=email,mobile=mobile,address=address)
        ob.save()
        return render(request,'contacts.html',{'output':'contact successfully...'})
    return render(request,'contacts.html')

def update(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        address=request.POST['address']
        ob=contact_master.objects.filter(email=email).update(name=name,email=email,mobile=mobile,address=address)
        return redirect('cviewdata')
    return render(request,'cviewdata.html')

def cviewdata(request):
    ob=contact_master.objects.all()
    if request.method=='POST':
        btn=request.POST['btn']
        if btn=='edit':
            email=request.POST['email']
            ob=contact_master.objects.get(email=email)
            return render(request,'cedit.html',{'data1':ob})
        if btn=='delete':
            email=request.POST['email']
            ob=contact_master.objects.get(emai=email).delete()
            return redirect('cviewdata')
    return render(request,'cviewdata.html',{'data':ob})
   