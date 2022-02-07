from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from english.models import MyUser, Teacher, Student, Course


class Command(BaseCommand):
    help = 'Work with db'

    def handle(self, *args, **options):
        # Удаление
        MyUser.objects.all().delete()
        Teacher.objects.all().delete()
        Student.objects.all().delete()
        Course.objects.all().delete()
        # Group.objects.all().delete()

        MyUser.objects.create_superuser('admin', 'admin@local.domain', 'admin')

        # Создание пользователей
        users = ['teacher1', 'teacher2', 'student1', 'student2']
        for user in users:
            user = MyUser.objects.create_user(username=user,
                                              email=f'{user}@local.domain',
                                              password=f'{user}123456')
            # Создание токенов пользователям
            token = Token.objects.create(user=user)
            print(token)

        # Назначение групп пользователям
        for user in users:
            if 'teacher' in user:
                u = MyUser.objects.get(username=user)
                Teacher.objects.create(user_id=u.id)
            if 'student' in user:
                u = MyUser.objects.get(username=user)
                Student.objects.create(user_id=u.id)

        # Добавить курсы
        for course_id in range(10):
            teacher_last = Teacher.objects.all().last()
            Course.objects.create(course_author_id=teacher_last.user_id,
                                  name=f'Новый супер курс {course_id}')

        print('done')
