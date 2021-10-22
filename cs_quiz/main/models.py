from django.db import models


class Quizes(models.Model):
    quiz_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date created")


class Questions(models.Model):
    question = models.CharField(max_length=100)
    opt_1 = models.CharField(max_length=100)
    opt_2 = models.CharField(max_length=100)
    opt_3 = models.CharField(max_length=100)
    ans = models.CharField(max_length=100)
    quiz = models.ForeignKey(Quizes, on_delete=models.CASCADE)
