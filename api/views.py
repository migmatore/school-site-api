from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from api.models import Test, Post, Subject
from api.serializers import TestSerializer, QuestionSerializer, AnswerSerializer, PostSerializer, PostPostSerializer, \
    SubjectSerializer, SubjectPostSerializer


class TestView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        tests = Test.objects.all()

        serializer = TestSerializer(tests, many=True)

        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class SubjectView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        subjects = Subject.objects.all()

        serializer = SubjectSerializer(subjects)

        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        subject = SubjectPostSerializer(data=request.POST)

        if subject.is_valid():
            subject.save()

            return Response({
                "message": f"Subject {request.POST.title} created"
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                "message": "Error"
            }, status=status.HTTP_404_NOT_FOUND)


class PostView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)

        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        pass
