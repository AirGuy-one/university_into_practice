from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Todo
from .forms import TodoForm


def index(request):
    item_list = Todo.objects.order_by("-updated_at")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Ваша запись была удалена !!!")
    return redirect('home')


def toggle_completed(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    item.completed = not item.completed
    item.save()
    return redirect('home')


