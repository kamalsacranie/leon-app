from main.models import Quiz, Questions
from django import forms


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = ["set_by", "pub_date"]


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
