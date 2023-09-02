from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"The usernme is already exist. Please try another one")
            #return redirect('home')
        elif User.objects.filter(email=email):
            messages.error(request,"The email is already registered! try another one")
           # return redirect('home')
        elif len(username)>10:
            messages.error(request,"The username must under 10 characters")
            
        elif pass1!=pass2:
            messages.error(request,"The password didn't match!")
        elif not username.isalnum():
            messages.error(request,"Please enter Alpha-NUmeric characters")


        else:
            myuser=User.objects.create_user(username,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request,"Your account has been successfully created")
            return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']

        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,'index.html',{'fname':fname})
        else:
            messages.error(request,"bad credentials")
            return redirect('home')

    

    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')
