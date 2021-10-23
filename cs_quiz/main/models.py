from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100)
    quiz_description = models.TextField(max_length=500)
    pub_date = models.DateTimeField("date created")

    def __str__(self):
        return self.quiz_name

    def get_questions(self):
        return self.question_set.all()


class Question(models.Model):
    question = models.CharField(max_length=100)
    opt_1 = models.CharField(max_length=100)
    opt_2 = models.CharField(max_length=100)
    opt_3 = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


# class QuizTask(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, null=True, blank=True
#     )
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     complete = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.quiz

#     class Meta:
#         ordering = ["complete"]


class UserQuizInfo(models.Model):
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()


class AssignedQuiz(models.Model):
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
