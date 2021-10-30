from .views import home_view, quiz_view, create_quiz_view

from django.urls import path

urlpatterns = [
    path("home/", home_view, name="home"),
    path("quiz/<pk>/", quiz_view, name="quiz"),
    path("create/", create_quiz_view, name="create-quiz"),
]
