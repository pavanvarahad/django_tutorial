from django.urls import path
from .views import dashboard, create_quiz

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("create-quiz/", create_quiz, name="create_quiz"),
]