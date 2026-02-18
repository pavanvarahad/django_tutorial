from django.urls import path
from .views import user_input_ui,process_input,show_output

urlpatterns = [
    path("",user_input_ui,name="user_input_ui"),
    path("process_input",process_input,name="process_input"),
    path("output",show_output,name="show_output")
]
