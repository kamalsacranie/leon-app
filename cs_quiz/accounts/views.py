from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .forms import SignUpForm
from main.models import AssignedQuiz


# def login(request):
#     return render(request, "accounts/login")


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
        form = SignUpForm()
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
def profile_view(request) -> HttpResponse:
    context = {
        "assigned_quizes": list(AssignedQuiz.objects.filter(user=request.user))
    }
    return render(request, "accounts/profile.html", context)
