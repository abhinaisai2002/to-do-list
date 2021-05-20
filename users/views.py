from django.shortcuts import render
from .forms import UserCreateForm
def register_view(request):
    form  = UserCreateForm()
    return render(request,'users/register.html',{'form':form})

def login_view(request):
    return render(request, 'users/login.html')