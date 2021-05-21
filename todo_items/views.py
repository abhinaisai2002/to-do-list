from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .forms import AddForm,UpdateItemForm
from . models import Items
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


@login_required(login_url='users:login')
def update_item_view(request,id):


    item = Items.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UpdateItemForm(instance=item)
        context = {
            'form' : form
        }
    return render(request, 'todo_items/update_item.html',context)


@login_required(login_url='users:login')
def delete_item_view(request,id):
    if request.method == 'POST':
        item = Items.objects.get(id=id)
        item.delete()
        return redirect('home')
    
    return render(request,'todo_items/delete_item.html')
