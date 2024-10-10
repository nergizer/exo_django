import datetime
from typing import List

from django.db import models
from django.utils import timezone


# Create your models here.
class Choice:
    pass


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def get_choices(self) -> List[Choice]:
        return Choice.objects.filter(question_id=self.id)

    def age(self) -> datetime.datetime:
        return timezone.now() - self.pub_date

    def __str__(self):
        return self.question_text

    def sum_votes(self) -> int:
        return sum(map(lambda v: v.votes, self.get_choices()))

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) and self.pub_date <= timezone.now()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def perc(self) -> int:
        if self.votes == 0:
            return 0
        return int((self.votes/self.question.sum_votes())*100)

    def __str__(self):
        return self.choice_text
