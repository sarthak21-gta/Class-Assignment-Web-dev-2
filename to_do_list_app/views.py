from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def add_task(request):
    return render(request,'add_task.html')
def edit(request):
    return render(request,'edit_task.html')