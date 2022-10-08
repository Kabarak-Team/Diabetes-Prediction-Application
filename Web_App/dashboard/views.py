from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')


def register(request):
    return render(request, 'dashboard/authentication-register.html')


def login(request):
    return render(request, 'dashboard/authentication-login.html')


def charts(request):
    return render(request, 'dashboard/charts.html')


def tables(request):
    return render(request, "dashboard/tables.html")


def chat(request):
    return render(request, "dashboard/chat.html")