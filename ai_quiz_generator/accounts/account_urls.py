from django.urls import path
from .views import register,login,dashboard

urlpatterns = [
    path("",register,name="register_page"),
    path("register/",register,name="register"),
    path("login/",login,name="login_page"),
    path("handle_login/",login,name="handle_login"),
    path("dashboard/",dashboard,name="dashboard")
]