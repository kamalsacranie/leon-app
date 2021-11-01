from datetime import datetime
from django.forms.widgets import NumberInput
from django.utils import timezone
from main.models import Quiz, Questions
from django import forms


class QuizForm(forms.ModelForm):
    due_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))

    class Meta:
        model = Quiz
        exclude = [
            "set_by",
            "pub_date",
        ]

    # The widget NumberInput already converst our form input to a date and
    # django expects a string so we have to specify this custom method to
    # override django's default behaviou
    def clean_due_date(self):
        date = self.cleaned_data["due_date"]
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date


class QuizQuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        exclude = ["quiz"]


class AnswersForm(forms.Form):
    CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")]
    q1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q3 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q4 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q5 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q6 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q7 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q8 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q9 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    q10 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        fields = (
            "q1",
            "q2",
            "q3",
            "q4",
            "q5",
            "q6",
            "q7",
            "q8",
            "q9",
            "q10",
        )
