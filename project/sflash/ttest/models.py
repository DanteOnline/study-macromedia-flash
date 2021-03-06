from django.db import models
from theory.models import Theory

# Create your models here.
class JuniorQuestion(models.Model):
    text = models.CharField(max_length=300)
    theme = models.ForeignKey(Theory)

    def get_answers(self):
        return JuniorAnswer.objects.filter(question = self)

    def __str__(self):
        return self.text

class JuniorAnswer(models.Model):
    text = models.CharField(max_length=500)
    question = models.ForeignKey(JuniorQuestion)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class SeniorQuestion(models.Model):
    text = models.CharField(max_length=200)
    theme = models.ForeignKey(Theory)

    def get_answers(self):
        return SeniorAnswer.objects.filter(question = self)

    def __str__(self):
        return self.text

class SeniorAnswer(models.Model):
    text = models.CharField(max_length=500)
    question = models.ForeignKey(SeniorQuestion)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class ProfiQuestion(models.Model):
    text = models.CharField(max_length=200, unique=True)
    theme = models.ForeignKey(Theory)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class QuestionAnswer:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.is_true = False


