from .views import home, quiz

# from django.contrib import admin
from django.urls import path

urlpatterns = [path("", home, name="home"), path("quiz/", quiz, name="quiz")]
