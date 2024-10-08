from django.contrib import admin

# Register your models here.
from .models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    ordering = ["pub_date"]
    date_hierarchy = "pub_date"
    search_fields = ["question_text"]

    list_filter = ["question_text"]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    ordering = ["question"]
    date_hierarchy = "question__pub_date"
    search_fields = ["choice_text","question__question_text"]

    list_filter = ["question","question__question_text"]



