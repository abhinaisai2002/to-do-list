from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import LoginForm, ProfileForm, UserCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserCreateForm(request.POST)
            if form.is_valid():
                form.save()
                username = request.user.username
                messages.success(request,f"Account created {username}")
                return redirect('users:login')
        else:
            form = UserCreateForm()
        context = {'form':form}
    return render(request,'users/register.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            user = authenticate(request,username=username,password=password,email=email)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))

                messages.success(request, "Logged In")
                return redirect('home')
            else:
                form = LoginForm(data = request.POST)
                return render(request,'users/login.html',{'form':form})
        else:
            form = LoginForm()
            context = {'form':form}
            return render(request, 'users/login.html',context)

def logout_view(request):
    user = request.user
    logout(request)
    return redirect('users:login')

@login_required(login_url='users:login')
def profile_view(request): 
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('users:profile')
    else:
        form = ProfileForm(instance=request.user)
        context = {
            'form' : form 
        }
        return render(request,'users/profile.html',context)
