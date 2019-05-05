from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from api.models import Test, Post
from api.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, PostSerializer


class TestView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        tests = Test.objects.all()

        serializer = TestSerializer(tests, many=True)

        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class PostView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)

        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
