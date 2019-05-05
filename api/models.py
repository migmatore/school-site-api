from django.contrib.auth.models import User, UserManager
from django.db import models


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


class Subject(models.Model):
    """Модель школьного предмета"""

    title = models.TextField("Название предмета", max_length=100)

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Post(models.Model):
    """Модель поста"""

    subject = models.ManyToManyField(Subject, verbose_name="Предмет", related_name="subject")
    title = models.TextField("Название поста", max_length=150)
    miniBody = models.TextField("Под заголовок", max_length=150)
    body = models.TextField("Содержание", max_length=700)
    author = models.TextField("Автор", max_length=100)
    date = models.DateField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
