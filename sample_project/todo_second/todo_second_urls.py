from django.urls import path
from .views import home,add_task,show_all_tasks,task_completed,delete_task

urlpatterns=[
    path("",home,name="home_page"),
    path("add_new_todo",add_task,name="add_task"),
    path("list",show_all_tasks,name="show_task"),
    path("task_completed/<int:task_sl_no>",task_completed,name="task_completed"),
    path("delete_task/<int:task_sl_no>",delete_task,name="delete_task")
]