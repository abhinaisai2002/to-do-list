
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='users:login')
def home_view(request):
    return render(request,'home.html',{})
    # http: // localhost: 8000/
