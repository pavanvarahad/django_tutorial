from django.shortcuts import render,redirect

todo_list = {
    "Complete Assignmnt": "INCOMPLETE",
    "Go to GYM": "INCOMPLETE"
}


# Create your views here.
def home_view(request):
    #  DISPLAY ALL THE TODO LISTS
    return render(request, 'todo/index.html',{'tasks':todo_list})

def add_new_task(request):
    new_task = request.POST.get('new_task')
    todo_list[new_task] = "INCOMPLETE"
    return redirect('home')

def delete(request):
    task_to_be_deleted = request.POST.get('delete_value')
    todo_list.pop(task_to_be_deleted)
    return redirect('home')

def mark_completed(request):
    task_to_be_completed = request.POST.get('completed_value')
    todo_list[task_to_be_completed] = "COMPLETE"
    print(todo_list)
    return redirect('home')

