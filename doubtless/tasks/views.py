from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {
        'tasks' : tasks,
    })

def remaining(request):
    return render(request, 'remaining.html')

def completed(request):
    return render(request, 'completed.html')

def add_task(request):
    return render(request, 'add_task.html')

def delete_task(request):
    return render(request, 'delete.html')

def task_detail(request):
    return render(request, 'task_detail.html')
