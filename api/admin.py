from django.contrib import admin

from api.models import *


class TestAdmin(admin.ModelAdmin):
    list_display = ("creator", "testTitle", "test_questions")

    def test_questions(self, obj):
        return "\n".join([question.questionTitle for question in obj.questions.all()])


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("questionTitle", "question_answers")

    def question_answers(self, obj):
        return "\n".join([answer.answerTitle for answer in obj.answers.all()])


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("answerTitle", )


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "required_posts")

    def required_posts(self, obj):
        return "\n".join([post.title for post in obj.post.all()])


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "miniBody", "body", "author")


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Post, PostAdmin)
