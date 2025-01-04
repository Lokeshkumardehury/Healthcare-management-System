from django.shortcuts import render,redirect
from signup.models import signup_master
# Create your views here.
def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            ob=signup_master.objects.get(email=email,password=password)
            request.session['name']=ob.name
            request.session['email']=ob.email
            request.session['mobile']=ob.mobile
            request.session['role_name']=ob.role_name
            if ob.role_name=='doctor':
                return redirect('dhome')
            
            elif ob.role_name=='patient':
                return redirect('phome')
            
            elif ob.role_name=='admin':
                return redirect('ahome')
            else:
                return render(request,'signin.html')
        except Exception as e:
            return render(request,'signin.html',{'output':'invalid' + str(e)})
    return render(request,'signin.html')