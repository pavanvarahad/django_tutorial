from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
# tasks =[
#     {
    # "task_name":"Learn Django",
#      "completed" : True
#     },
# ]
all_tasks = []

# Create your views here.
def home(request):
    return render(request,"todo_second/index.html")

def show_all_tasks(request):
    return render(request,"todo_second/list.html",{"all_tasks":all_tasks})

def add_task(request):
    print(type(request))
    new_task = request.POST.get("task")
    task_dictionary = {
        "task_name": new_task,
        "completed": False
    }
    Todo.objects.create(id=2,task_name=new_task,is_completed=False)
    all_tasks.append(task_dictionary)
    print("-"*80)
    print(all_tasks)
    print("-"*80)
    return redirect("show_task")

def task_completed(request,task_sl_no):
    all_tasks[task_sl_no-1]["completed"] = True
    return redirect("show_task")

def delete_task(request,task_sl_no):
    all_tasks.pop(task_sl_no-1)
    return redirect("show_task")
    