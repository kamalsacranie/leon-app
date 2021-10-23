from main.models import Quiz, Questions
from django.forms import ModelForm


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        exclude = ["set_by", "pub_date"]


class QuizQuestionsForm(ModelForm):
    class Meta:
        model = Questions
        exclude = ["quiz"]
