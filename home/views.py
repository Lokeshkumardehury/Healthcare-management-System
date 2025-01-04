from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('<h1><b>welcome to homepage....</b></h1>')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    return render(request,'register.html')

def gallery(request):
    return render(request,'gallery.html')

def faq(request):
    return render(request,'faq.html')

def login(request):
    return render(request,'login.html')


def coursedetails(request,courseid):
    return HttpResponse(courseid)

