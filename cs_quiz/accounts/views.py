from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
)
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy

from main.models import UserQuizInfo
from main.models import Quiz
from .forms import SignUpForm


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("password-success")


def password_change_success_view(request):
    return render(request, "accounts/password_change_success.html", {})


# If we were to just use usercreationform as a function view
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
    else:
        # If its a get request we get our form
        form = UserCreationForm()
    # We reutn a rendered bit fo html
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return render(request, "main/home.html", {})


@login_required
def profile_view(request, pk) -> HttpResponse:
    # getting our queryset of all quizes
    quizes = Quiz.objects.all().order_by("-due_date")
    # Getting our user specific info for all the quizes
    user_info = UserQuizInfo.objects.filter(user_id=pk)
    # Tupel of quiz ids
    user_quiz_ids = [i.quiz_name_id for i in user_info]
    user_quizes = dict()

    for quiz in quizes:
        if quiz.id in user_quiz_ids:
            # if the user has a score for the current quiz in the databese,
            # then we add that quizinfoobject to our dictionary
            user_quizes[quiz.quiz_name] = UserQuizInfo.objects.filter(
                user_id=pk, quiz_name_id=quiz.id
            )[0]
        else:
            user_quizes[quiz.quiz_name] = Quiz.objects.filter(id=quiz.id)[0]

    # print("UserQz", user_quizes)
    context = {
        "user_quizes": user_quizes,
        "quizes": {quiz.id: quiz for quiz in Quiz.objects.all()},
    }
    return render(request, "accounts/profile.html", context)
