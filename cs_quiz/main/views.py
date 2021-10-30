from django.contrib.auth.models import User
from main.forms import QuizQuestionsForm, QuizForm, AnswersForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
import random


from .models import Questions, Quiz, UserQuizInfo


def questions_stripper(questions: dict) -> tuple[list, dict]:
    keys = [key for key in questions.keys() if type(questions[key]) is str]
    keys = [
        key for key in keys if "_" not in key and len(key) < 4 and "q" in key
    ]
    return keys, {key: questions[key] for key in keys}


def key_parser(key: str) -> str:
    key = (
        key.replace("q", "question ")
        if "_" not in key
        else key.replace("_", " ").replace("opt", "option")
    )
    key = key.replace("ans", "answer") if "ans" in key else key
    return key


# Create your views here.
def home_view(request) -> HttpResponse:
    context = {"my_var": "This is the variable"}
    return render(request, "main/home.html", context)


def quiz_view(request, pk) -> HttpResponse:
    # Getting our quiz that was clicked on by the user by filtering our model
    # by the quiz pk
    quiz = Quiz.objects.filter(id=pk)[0]

    print(12)
    ui_query = UserQuizInfo.objects.filter(
        quiz_name_id=pk, user_id=request.user.id
    )
    user_info = ui_query[0] if ui_query else None
    print(user_info)
    try:
        questions = Questions.objects.filter(quiz_id=pk)[0].__dict__
        # Get our question keys in the correct order
        q_keys, q_dict = questions_stripper(questions)
        # Randomise our quesiton order so that we randomise where our answer is
        random_keys = list(questions.keys())
        # Happens in place for some reason
        random.shuffle(random_keys)
        # Create new dict for our reordered keys
        final_questions = dict()
        for q_key in q_keys:
            final_questions[q_key] = {
                key: questions[key]
                for key in random_keys
                if q_key in key
                and q_key != key
                and len([s for s in q_key if s.isnumeric()])
                == len([s for s in key[0:3] if s.isnumeric()])
            }
        print(final_questions)
        answer_order = list()
        for key in final_questions.keys():
            answer_number = [
                i
                for i, e in enumerate(final_questions[key].keys())
                if "ans" in e
            ][0] + 1
            answer_order.append(answer_number)
        print(answer_order)

    except IndexError:
        final_questions = None
        q_dict = None

    if request.method == "POST":
        answers_form = AnswersForm(request.POST)
        if answers_form.is_valid():
            answers = answers_form.cleaned_data
            user_answer_order = [answers[k] for k in answers.keys()]
            print(user_answer_order)
            num_correct = len(
                [
                    a
                    for a, b in zip(answer_order, user_answer_order)
                    if a == int(b)
                ]
            )
            score = num_correct / 10
            result = UserQuizInfo(
                quiz_name=quiz,
                user=request.user,
                score=score,
            )
            result.save()
            print(user_answer_order)
            return redirect("home")
    else:
        answers_form = AnswersForm()

    context = {
        "quiz": quiz,
        "ui": user_info,
        "q_dict": q_dict,
        "questions": final_questions,
        "form": answers_form,
    }

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
