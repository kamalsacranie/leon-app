from . import views

from django.urls import path

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("quiz/<pk>/", views.quiz_view, name="quiz"),
    path("scores/", views.user_score_view, name="user-scores"),
    path("all_scores/", views.admin_score_view, name="admin-scores"),
    path("create/", views.create_quiz_view, name="create-quiz"),
]
