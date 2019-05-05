from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "answerTitle", "selected")


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ("id", "questionTitle", "answers")


class TestSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ("id", "creator", "testTitle", "questions")
