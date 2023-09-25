from django.shortcuts import render
from app1.models import places
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# def home(request):
#     return render(request,'home.html')
def view(request):
    k = places.objects.all()
    return render(request,'home.html',{'k':k})

def sign_up(request):
    if request.method=='POST':
        u = request.POST['u']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        u = User.objects.create_user(username=u,first_name=f,last_name=l,email=e,password=p)
        u.save()

    return render(request,'signup.html')


def log_in(request):
    if(request.method=='POST'):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            return view(request)
        else:
            messages.error(request,"invalid credentrials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return log_in(request)