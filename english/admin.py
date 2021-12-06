from django.contrib import admin
from english.models import MyUser, Students, Teachers, Scores, Groups, Courses, Schedule


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = "id", "username", "first_name", "last_name"


admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Groups)
admin.site.register(Scores)
admin.site.register(Courses)
admin.site.register(Schedule)