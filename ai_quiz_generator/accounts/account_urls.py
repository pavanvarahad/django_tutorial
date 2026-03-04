from django.urls import path
from .views import register

urlpatterns = [
    path("",register,name="register_page"),
    path("/register",register,name="register")
]