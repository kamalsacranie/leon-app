from . import views

# from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/<pk>/", views.profile_view, name="profile"),
    path(
        "password/",
        views.PasswordsChangeView.as_view(
            template_name="accounts/change_password.html",
        ),
        name="password",
    ),
    path(
        "password-change-success/",
        views.password_change_success_view,
        name="password-success",
    ),
]
