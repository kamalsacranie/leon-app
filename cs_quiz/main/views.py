from django.http import HttpResponse
from django.shortcuts import render


from .models import Quiz


# Create your views here.
def home(request) -> HttpResponse:
    context = {"my_var": "This is the variable"}
    return render(request, "main/home.html", context)


def quiz(request) -> HttpResponse:
    context = {"quizes": Quiz.objects.all()}
    return render(request, "main/quiz.html", context)
