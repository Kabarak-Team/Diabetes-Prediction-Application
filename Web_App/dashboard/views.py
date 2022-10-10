from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')


def register(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Username = request.POST['Username']
        Email = request.POST['Email']
        Password1 = request.POST['Password1']  
        Password2 = request.POST['Password2']
        
        
        if Password1 == Password2:
            if User.objects.filter(Name=Name).exists():
                messages.info(request,'Username Taken!')
                return redirect('register')
            elif User.objects.filter(Email=Email).exists():
                messages.info(request,'Email Exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(Name=Name, Username=Username, Email=Email, password=Password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching!')
            return redirect('register')
    else:
        return render(request, 'dashboard/authentication-register.html')


def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        user = auth.authenticate(Username=Username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'dashboard/authentication-login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def charts(request):
    return render(request, 'dashboard/charts.html')


def about(request):
    return render(request, 'dashboard/about.html')


def team(request):
    return render(request, 'dashboard/team.html')


def contact(request):
    return render(request, 'dashboard/contact.html')
