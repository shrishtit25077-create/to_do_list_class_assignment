
from django.shortcuts import render,redirect
from .models import Task

def home(request):
    data = Task.objects.all()
    return render(request, 'home.html',{'data':data})
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

def edit_task(request):
    return render(request, 'edit_task.html')