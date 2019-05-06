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


class SubjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectCategory
        fields = ("id", "title")


class PostSerializer(serializers.ModelSerializer):
    subject_category = SubjectCategorySerializer()

    class Meta:
        model = Post
        fields = ("subject_category", "id", "title", "mini_body", "body", "author", "date")


class SubjectCategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectCategory
        fields = ("title", )


class PostPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("subject_category", "title", "mini_body", "body", "author")
