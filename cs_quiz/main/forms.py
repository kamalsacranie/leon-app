from main.models import Quiz, Questions
from django.forms import ModelForm


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ["quiz_name", "quiz_description", "pub_date", "set_by"]


class QuizQuestionsForm(ModelForm):
    class Meta:
        model = Questions
        exclude = []
