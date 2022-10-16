from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')  
        password2 = request.POST.get('password2')
        
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
               messages.info(request,'Username Taken')
               return redirect('register')
            
            elif User.objects.filter(email = email).exists():
                 messages.info(request,'Email Taken')
                 return redirect('register')
            else:    
                user = User.objects.create_user(name = name, username = username, password = password1, email = email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching!')
            return redirect('register')
    else:
        return render(request, 'dashboard/authentication-register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        
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
