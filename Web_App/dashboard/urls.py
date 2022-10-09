from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
    path('', views.index, name='index'),
    path('charts', views.charts, name='charts'),
    path('logout', views.logout, name='logout'),
]