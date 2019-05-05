from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from api.models import Test, Question, Answer
from api.serializers import TestSerializer, QuestionSerializer, AnswerSerializer


class TestView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        rooms = Test.objects.all()

        serializer = TestSerializer(rooms, many=True)

        return Response({
            "data": serializer.data
        })


