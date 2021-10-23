from main.models import Quiz
from django.forms import ModelForm


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ["quiz_name", "quiz_description", "pub_date", "set_by"]
