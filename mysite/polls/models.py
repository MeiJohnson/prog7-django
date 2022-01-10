import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Здесь находятся модели запросов в БД

# Модель добавления вопроса
class Question(models.Model):
    def __str__(self): # Метод для вывода текста вопроса
        return self.question_text
    question_text = models.CharField(max_length=200) # Поле с текстом вопроса с макс длиной 200 символов
    pub_date = models.DateTimeField('date published') # Поле с датой добавления вопроса
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# Модель добавления варианта ответа
class Choice(models.Model):
    def __str__(self):
        return self.choice_text  # Метод для вывода текста варианта ответа
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Ключ, связывающий вариант ответа с вопросом
    choice_text = models.CharField(max_length=200) # Поле текста
    votes = models.IntegerField(default=0) # Поле числа голосов

