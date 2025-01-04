from django.shortcuts import render
from .models import profile_master
from signup.models import signup_master

# Create your views here.
def viewprofile(request):
    ob=profile_master.objects.all()
    return render(request,'view.html',{'data':ob})

def profile_page(request):

    if request.method=="POST":
        email=request.session.get('email')
        fname=request.POST['fname']
        lname=request.POST['lname']
        image=request.FILES['image']
        document=request.FILES['doc']
        address=request.POST['address']

        obj=signup_master.objects.get(email=email)
        profile,created=profile_master.objects.get_or_create(
        email=obj,
        defaults={
            'fname':fname,
            'lname':lname,
            'image':image,
            'document':document,
            'address':address,
        }
        )
        if not created:
            profile.fname=fname
            profile.lname=lname
            if image:
                profile.image=image
            if document:
                profile.document=document
            profile.address=address
            profile.save()
        # ob=profile_master.objects.create(email=obj,fname=fname,lname=lname,image=image,document=document,address=address)
        # ob.save()
        return render(request,'profile.html',{'data':"profile update sucessfuly"})
    
    return render(request,'profile.html')
