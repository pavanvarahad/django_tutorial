from django.shortcuts import render
from django.http import HttpResponse

# tasks =[
#     {"task_name":"Learn Django",
#      "completed" : True
#     },
# ]
tasks = []

# Create your views here.
def home(request):
    return render(request,"todo_second/index.html")

def add_task(request):
    new_task = request.POST.get('task')
    task_dictionary = {
        "task_name": new_task,
        "completed": False
    }
    tasks.append(task_dictionary)
    print("-"*80)
    print(tasks)
    print("-"*80)
    return HttpResponse(tasks)
    