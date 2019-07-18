from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from api.models import Test, Post, SubjectCategory
from api.serializers import (
    TestSerializer, PostSerializer, PostPostSerializer,
    SubjectCategorySerializer, SubjectCategoryPostSerializer
)


class TestView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        tests = Test.objects.all()

        serializer = TestSerializer(tests, many=True)

        return Response({
            "response": serializer.data
        }, status=status.HTTP_200_OK)


class SubjectCategoryView(APIView):
    permission_classes = [permissions.AllowAny, ]

#     @method_decorator(cache_page(60 * 60 * 2))
#     @method_decorator(vary_on_cookie)
    def get(self, request):
        subjects = SubjectCategory.objects.all()

        serializer = SubjectCategorySerializer(subjects, many=True)

        return Response({
            "response": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        subject = SubjectCategoryPostSerializer(data=request.POST)

        if subject.is_valid():
            subject.save()

            return Response({
                "response": "Subject created"
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                "response": "Error!"
            }, status=status.HTTP_404_NOT_FOUND)


# Base post view(getting all posts and create new)
class PostView(APIView):
    permission_classes = [permissions.AllowAny, ]

    # Get all posts
    def get(self, request):
        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)

        return Response({
            "response": serializer.data
        }, status=status.HTTP_200_OK)

    # Create post
    def post(self, request):
        post = PostPostSerializer(data=request.POST)

        if post.is_valid():
            post.save()

            return Response({
                "response": f"Post created"
            }, status=status.HTTP_201_CREATED)

        else:
            return Response({
                "response": "Error!"
            }, status=status.HTTP_404_NOT_FOUND)


# Post detail view(getting a post by id and it's details)
class PostDetailView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, pk):
        post = Post.objects.filter(id=pk)

        serializer = PostSerializer(post, many=True)

        return Response({
            "response": serializer.data
        }, status=status.HTTP_200_OK)


# In Develop
# TODO: implement post editing
# Post edit view(editing post)
class PostEditView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, pk):
        pass


# Subject posts view(getting subject posts)
class SubjectPostsView(APIView):
    permission_classes = [permissions.AllowAny, ]

#     @method_decorator(cache_page(60 * 60 * 2))
#     @method_decorator(vary_on_cookie)
    def get(self, request, pk):
        posts = Post.objects.filter(subject_category=pk)

        serializer = PostSerializer(posts, many=True)

        return Response({
            "response": serializer.data
        }, status=status.HTTP_200_OK)
