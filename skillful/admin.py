from django.contrib import admin

from skillful.models import Test, Answer, Question, TestTaken, Subject


class TestAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'subject', 'image', 'difficulty_level', 'time_interval', 'time_between_attempts']
    readonly_fields = []
    list_display = ['title', 'description', 'subject', 'image', 'time_interval', 'time_between_attempts']


class AnswerAdmin(admin.ModelAdmin):
    fields = ['text', 'is_correct', 'question']
    readonly_fields = []
    list_display = ['text', 'is_correct', 'question']


class QuestionAdmin(admin.ModelAdmin):
    fields = ['code', 'is_multiple_choice', 'type', 'test']
    readonly_fields = []
    list_display = ['code', 'is_multiple_choice', 'type', 'test']


class TestTakenAdmin(admin.ModelAdmin):
    fields = ['short_info', 'public', 'result', 'canceled', 'created_at', 'test', 'user']
    readonly_fields = []
    list_display = ['short_info', 'public', 'result', 'canceled', 'created_at', 'test', 'user']


class SubjectAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'image']
    readonly_fields = []
    list_display = ['title', 'description', 'image']


admin.site.register(Test, TestAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(TestTaken, TestTakenAdmin)
admin.site.register(Subject, SubjectAdmin)


admin.site.site_header = 'Skill Tester'
admin.site.site_title = 'Skill Tester'
admin.site.index_title = 'Admin Dashboard'
