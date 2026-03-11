from django.urls import path
from .views import dashboard, create_quiz, submit_quiz

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("create-quiz/", create_quiz, name="create_quiz"),
    path("submit-quiz/", submit_quiz, name="submit_quiz"),
]
