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


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "title")


class SubjectPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("title",)


class PostSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True)

    class Meta:
        model = Post
        fields = ("subject", "title", "miniBody", "body", "author", "date")


class PostPostSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(many=True)

    class Meta:
        model = Post
        fields = ("subject", "title", "miniBody", "body", "author")
