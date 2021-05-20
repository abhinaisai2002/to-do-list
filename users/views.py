from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .forms import LoginForm, UserCreateForm
from django.contrib import messages

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserCreateForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,f"Account created for {username}")
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
                messages.success(request, "Logged In")
                return redirect('home')
        else:
            form = LoginForm()
        context = {'form':form}
        return render(request, 'users/login.html',context)

def logout_view(request):
    user = request.user
    logout(request)
    return redirect('users:login')
