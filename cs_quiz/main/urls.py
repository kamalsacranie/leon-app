from .views import home, quiz

from django.urls import path

urlpatterns = [
    path("home/", home, name="home"),
    path("quiz/", quiz, name="quiz"),
]
