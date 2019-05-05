from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    """Модель ответа"""

    answerTitle = models.TextField("Текст ответа", max_length=150)
    selected = models.BooleanField("Выбрано", default=False)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


class Question(models.Model):
    """Модель вопроса"""

    questionTitle = models.TextField("Текст вопроса", max_length=150)
    answers = models.ManyToManyField(Answer, verbose_name="Ответы", related_name="answers")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Test(models.Model):
    """Модель теста"""

    creator = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE)
    testTitle = models.TextField("Название теста", max_length=100)
    questions = models.ManyToManyField(Question, verbose_name="Вопросы", related_name="questions")

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


