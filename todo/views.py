from django.shortcuts import render, redirect, get_object_or_404 
from .models import item
from .forms import itemForm

# Create your views here.


def getToDoList(request):
    items = item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == "POST":
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getToDoList')
    form = itemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    item_get = get_object_or_404(item, id=item_id)
    if request.method == "POST":
        form = itemForm(request.POST, instance=item_get)
        if form.is_valid():
            form.save()
            return redirect('getToDoList')
    form = itemForm(instance=item_get)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def delete_item(request, item_id):
    item_get = get_object_or_404(item, id=item_id)
    item.delete(item_get)
    return redirect('getToDoList')
