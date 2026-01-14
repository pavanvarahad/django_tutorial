from .views import calculator_view
from django.urls import path

urlpatterns = [
    path("abc", calculator_view, name="calculator_home"),
]