import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    """ The question model for poll questions """
    question_text = models.CharField(max_length=1024)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        """ Checks if the questiion was recently published """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """ Represents the options for a question """
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice_text = models.CharField(
        max_length=1024,
    )
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
