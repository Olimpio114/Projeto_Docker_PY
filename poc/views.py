
from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')

    tasks = Task.objects.all().order_by('-created')
    context = {'tasks': tasks}
    return render(request, 'poc/task_list.html', context)