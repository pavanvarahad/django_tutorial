from django.urls import path
from .views import home_view,add_new_task,delete,mark_completed

urlpatterns = [
    path('', home_view, name='home'),
    path('add_task', add_new_task, name='add_task'),
    path('delete_task',delete, name="delete"),
    path('completed',mark_completed, name="completed")
]