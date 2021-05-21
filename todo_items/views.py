from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .forms import AddForm
# Create your views here.


@login_required(login_url='users:login')
def add_item_view(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
    else:
        form = AddForm()
        context = {
            'form':form
        }
        return render(request,'todo_items/add_item.html',context)

def update_item_view(request):
    return render(request, 'todo_items/update_item.html')
