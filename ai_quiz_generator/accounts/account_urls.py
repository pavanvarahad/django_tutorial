from django.urls import path
from .views import register,handle_login,handle_logout

urlpatterns = [
    path("",register,name="register_page"),
    path("register/",register,name="register"),
    path("login/",handle_login,name="login_page"),
    path("handle_login/",handle_login,name="handle_login"),
    path("logout/",handle_logout,name="handle_logout")
]