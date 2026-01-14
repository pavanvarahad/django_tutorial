from .views import calculator_view
from django.urls import path

urlpatterns = [
    path("", calculator_view, name="calculator_home"),
]