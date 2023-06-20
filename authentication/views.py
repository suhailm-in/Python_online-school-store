from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
import authentication.apps


def login(request):
    if request.method=='POST':
        username=request.POST['your_name']
        password=request.POST['your_pass']
        print(f"Received username: {username}, password: {password}")
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("User authenticated and logged in")
            return redirect('/')
        else:
            messages.info(request,"invalid username or password")
            print("Authentication failed")
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass']
        repass=request.POST['re_pass']
        if password==repass:
            if User.objects.filter(username=name).exists():
                messages.info(request,"username is taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is taken")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=name,email=email,password=password)

                user.save();
                return redirect('login')
                # print("User Created")
        else:
            messages.info(request, "Password not macthing")
            return redirect('signup')
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')