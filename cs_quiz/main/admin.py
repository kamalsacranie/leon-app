from django.contrib import admin
from .models import Questions, Quiz, UserQuizInfo

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(UserQuizInfo)
