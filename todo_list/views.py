
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from todo_items.models import Items

@login_required(login_url='users:login')
def home_view(request):
    items = Items.objects.filter(user = request.user)
    context = {
        'items' : items
    }
    return render(request,'home.html',context)
    # http: // localhost: 8000/
