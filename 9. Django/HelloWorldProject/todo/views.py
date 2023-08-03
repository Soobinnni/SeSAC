from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from .models import Task
# Create your views here.
def task_list(request:HttpRequest)-> HttpResponse :
    task = Task.objects.all()
    return render(request, "todo/task_list.html", {'task': task})

def task_create(request:HttpRequest)-> HttpResponse :
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task.objects.create(title = title, description = description)
        task.save()
        return redirect('task_detail', task.pk)
    return render(request, "todo/task_create.html")

def task_detail(request:HttpRequest, pk:int)-> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    return render(request, "todo/task_detail.html", {'task' : task})

def task_update(request:HttpRequest, pk:int)-> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST' :
        title = request.POST['title']
        description = request.POST['description']
        # completed = bool(request.POST['completed'])
        task.title = title
        task.description = description
        # task.completed = completed
        task.save()

        return redirect('task_detail', task.pk)
    return render(request, "todo/task_update.html", {'task' : task})

def task_delete(request:HttpRequest, pk:int)-> HttpResponse:
    task = Task.objects.get(pk=pk)
    print(task)
    task.delete()
    return redirect('task_list')