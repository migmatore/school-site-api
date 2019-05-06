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
    list_display = ("id", "title")


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "subject_category", "title", "mini_body", "body", "author")

    def subject_category(self, obj):
        return "\n".join([category.title for category in obj.subject_category.all()])


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

admin.site.register(SubjectCategory, SubjectAdmin)
admin.site.register(Post, PostAdmin)
