from django.urls import path
from .views import home,add_task

urlpatterns=[
    path("/",home,name="home_page"),
    path("/add_new_todo",add_task,name="add_task")
]