from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo

# Create your views here.
def home(request):
    return render(request,"todo_second/index.html")

def show_all_tasks(request):
    all_db_rows = Todo.objects.all().values()
    return render(request,"todo_second/list.html",{"all_tasks":all_db_rows})

def add_task(request):
    new_task = request.POST.get("task")
    Todo.objects.create(task_name=new_task,is_completed=True)
    return redirect("show_task")

def task_completed(request,task_sl_no):
    selected_task = Todo.objects.get(id=task_sl_no)
    selected_task.is_completed = True
    selected_task.save()
    return redirect("show_task")

def delete_task(request,task_sl_no):
    selected_task_to_delete = Todo.objects.get(id=task_sl_no)
    selected_task_to_delete.delete()
    return redirect("show_task")
    