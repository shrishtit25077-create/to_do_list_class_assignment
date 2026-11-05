from django.shortcuts import render, redirect
from .models import Task


def home(request):
    data = Task.objects.all()

    return render(request, 'home.html', {'data': data})


def add_task(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            Task.objects.create(
                title=title,
                description=description
            )

            return redirect('home')

    return render(request, 'add_task.html')


def edit_task(request, id):

    task = Task.objects.get(id=id)

    if request.method == 'POST':

        task.title = request.POST.get('title')
        task.description = request.POST.get('description')

        task.save()

        return redirect('home')

    return render(request, 'edit_task.html', {'task': task})


def complete_task(request, id):

    task = Task.objects.get(id=id)

    if request.method == 'POST':

        task.completed = not task.completed
        task.save()

    return redirect('home')


def delete_task(request, id):

    task = Task.objects.get(id=id)

    if request.method == 'POST':

        task.delete()

    return redirect('home')