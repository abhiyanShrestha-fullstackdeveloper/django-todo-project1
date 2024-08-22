from django.shortcuts import render
from .models import Todo

# Create your views here.

def home(request):
    todo_objs = Todo.objects.all() # Runs all the query from the todo table
    data = {'todos': todo_objs} # Send file from data variable as support 
    return render(request,'index.html',context=data)

def create(request):
    return render(request,'create.html')
