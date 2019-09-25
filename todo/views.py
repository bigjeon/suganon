from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect

def todoview(request):
    all_todo_items=TodoItem.objects.all()
    return render(request, 'todo/todo.html', {'all_items':all_todo_items})

def tododelete(request, todo_id):
    delete_item=TodoItem.objects.get(id = todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')

def todoadd(request):
    new_todo=TodoItem(content=request.POST['content'])
    new_todo.save()
    return HttpResponseRedirect('/todo/')