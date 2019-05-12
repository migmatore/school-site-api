from django.urls import path

from api.views import *

urlpatterns = [
    path('test/', TestView.as_view()),
    path('post/', PostView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view()),
    path('subject/', SubjectCategoryView.as_view()),
    path('subject/<int:pk>', SubjectPostsView.as_view())
]
