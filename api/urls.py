from django.urls import path

from api.views import TestView, PostView, SubjectCategoryView, PostDetailView

urlpatterns = [
    path('test/', TestView.as_view()),
    path('post/', PostView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view()),
    path('subject/', SubjectCategoryView.as_view())
]
