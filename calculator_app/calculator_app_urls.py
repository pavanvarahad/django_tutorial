from .views import calculator_view, jinja_tutorial
from django.urls import path

urlpatterns = [
    path("", calculator_view, name="calculator_home"),
    path("jinja/", jinja_tutorial, name="jinja_tutorial"),
]