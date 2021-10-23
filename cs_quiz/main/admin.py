from django.contrib import admin
from .models import AssignedQuiz, Question, Quiz, UserQuizInfo

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(UserQuizInfo)
admin.site.register(AssignedQuiz)
