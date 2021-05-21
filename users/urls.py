from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('register/',views.register_view,name = 'register'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('',include('todo_items.urls'))
]
