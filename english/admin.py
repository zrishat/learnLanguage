from django.contrib import admin
from english.models import MyUser, Student, Teacher, Score, Group, Course, Schedule


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = "id", "username", "first_name", "last_name"


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Score)
admin.site.register(Course)
admin.site.register(Schedule)
