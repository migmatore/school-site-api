from django.urls import path

from api.views import TestView, PostView, SubjectView

urlpatterns = [
    path('test/', TestView.as_view()),
    path('post/', PostView.as_view()),
    path('subject/', SubjectView.as_view())
]
