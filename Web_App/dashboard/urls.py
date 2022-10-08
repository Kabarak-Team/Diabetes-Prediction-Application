from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
]
