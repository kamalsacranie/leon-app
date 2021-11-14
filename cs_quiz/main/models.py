from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100)
    quiz_description = models.TextField(max_length=500)
    pub_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateField()
    set_by = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.quiz_name

    class Meta:
        verbose_name_plural = "Quizes"


class Questions(models.Model):
    q1 = models.CharField(max_length=100)
    q1_opt_1 = models.CharField(max_length=100)
    q1_opt_2 = models.CharField(max_length=100)
    q1_opt_3 = models.CharField(max_length=100)
    q1_ans = models.CharField(max_length=100)

    q2 = models.CharField(max_length=100)
    q2_opt_1 = models.CharField(max_length=100)
    q2_opt_2 = models.CharField(max_length=100)
    q2_opt_3 = models.CharField(max_length=100)
    q2_ans = models.CharField(max_length=100)

    q3 = models.CharField(max_length=100)
    q3_opt_1 = models.CharField(max_length=100)
    q3_opt_2 = models.CharField(max_length=100)
    q3_opt_3 = models.CharField(max_length=100)
    q3_ans = models.CharField(max_length=100)

    q4 = models.CharField(max_length=100)
    q4_opt_1 = models.CharField(max_length=100)
    q4_opt_2 = models.CharField(max_length=100)
    q4_opt_3 = models.CharField(max_length=100)
    q4_ans = models.CharField(max_length=100)

    q5 = models.CharField(max_length=100)
    q5_opt_1 = models.CharField(max_length=100)
    q5_opt_2 = models.CharField(max_length=100)
    q5_opt_3 = models.CharField(max_length=100)
    q5_ans = models.CharField(max_length=100)

    q6 = models.CharField(max_length=100)
    q6_opt_1 = models.CharField(max_length=100)
    q6_opt_2 = models.CharField(max_length=100)
    q6_opt_3 = models.CharField(max_length=100)
    q6_ans = models.CharField(max_length=100)

    q7 = models.CharField(max_length=100)
    q7_opt_1 = models.CharField(max_length=100)
    q7_opt_2 = models.CharField(max_length=100)
    q7_opt_3 = models.CharField(max_length=100)
    q7_ans = models.CharField(max_length=100)

    q8 = models.CharField(max_length=100)
    q8_opt_1 = models.CharField(max_length=100)
    q8_opt_2 = models.CharField(max_length=100)
    q8_opt_3 = models.CharField(max_length=100)
    q8_ans = models.CharField(max_length=100)

    q9 = models.CharField(max_length=100)
    q9_opt_1 = models.CharField(max_length=100)
    q9_opt_2 = models.CharField(max_length=100)
    q9_opt_3 = models.CharField(max_length=100)
    q9_ans = models.CharField(max_length=100)

    q10 = models.CharField(max_length=100)
    q10_opt_1 = models.CharField(max_length=100)
    q10_opt_2 = models.CharField(max_length=100)
    q10_opt_3 = models.CharField(max_length=100)
    q10_ans = models.CharField(max_length=100)

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Quiz Qestions"


class UserQuizInfo(models.Model):
    quiz_name = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    completion_date = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "User Quiz Info"
        verbose_name_plural = "Users Quiz Info"
