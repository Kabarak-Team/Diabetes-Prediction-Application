from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('register',views.register, name='register'), #127.0.0.1:8000/register
    path('login', views.login, name='login'),
    path('', views.index, name='index'),
    path('charts', views.charts, name='charts'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),
]