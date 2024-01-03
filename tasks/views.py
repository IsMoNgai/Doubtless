from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all().order_by('-id')
    return render(request, 'index.html', {
        'tasks' : tasks,
    })

def remaining(request):
    remaining_tasks = Task.objects.filter(completed = False)
    return render(request, 'remaining.html', {
        'remaining_tasks' : remaining_tasks,
    })

def completed(request):
    completed_tasks = Task.objects.filter(completed = True)
    return render(request, 'completed.html', {
        'completed_tasks' : completed_tasks,
    })

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        completed = False

        if title != "" and due_date != "" and due_time != "":
            task = Task(
                title = title,
                description = description,
                due_date = due_date,
                due_time = due_time,
                completed = completed
            )
            task.save()
            return redirect('home')
    else:
        return render(request, 'add_task.html')

    return render(request, 'add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'delete.html', {
        "task":task,
    })

def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task_detail.html', {
        "task":task,
    })

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        # Redirect to the previous view
        previous_url = request.META.get('HTTP_REFERER')
        if previous_url:
            return redirect(previous_url)
        else:
            # Fallback to a default URL if the referrer is not available
            return redirect('home')

def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('home')

