from main.forms import QuizForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test


from .models import Quiz


# Create your views here.
def home_view(request) -> HttpResponse:
    context = {"my_var": "This is the variable"}
    return render(request, "main/home.html", context)


def quiz_view(request) -> HttpResponse:
    context = {"quizes": Quiz.objects.all()}
    return render(request, "main/quiz.html", context)


@user_passes_test(lambda u: u.is_superuser)
def create_quiz_view(request):
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        # If its a get request we get our form
        form = QuizForm()
    # We reutn a rendered bit fo html
    return render(request, "main/create-quiz.html", {"form": form})
