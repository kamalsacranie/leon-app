from django.contrib.auth.models import User
from main.forms import QuizQuestionsForm, QuizForm
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
        quiz_form = QuizForm(request.POST)
        quiz_questions_form = QuizQuestionsForm(request.POST)
        if quiz_form.is_valid() and quiz_questions_form.is_valid():
            # This just a djando quirk
            quiz = quiz_form.save(commit=False)
            # Fill in our invisible fields with the necessary data
            quiz.set_by = User.objects.get(username=request.user)
            # Saving commits this to our database
            quiz.save()
            # do the same false commit so we can edit it
            questions = quiz_questions_form.save(commit=False)
            # We assign the quiz name as the FK
            questions.quiz = quiz
            quiz_questions_form.save()
            return redirect("home")
    else:
        # If its a get request we get our form
        quiz_form = QuizForm()
        quiz_questions_form = QuizQuestionsForm()
    # We reutn a rendered bit fo html
    return render(
        request,
        "main/create-quiz.html",
        {"quiz_form": quiz_form, "quiz_questions_form": quiz_questions_form},
    )
