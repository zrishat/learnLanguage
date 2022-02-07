from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)


class Teacher(models.Model):
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                primary_key=True)
    is_teacher = models.BooleanField(default=True)


class Group(models.Model):
    groupName = models.TextField(default='english low 2021.08')
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    LEVEL_LOW = 'L'
    LEVEL_MED = 'M'
    LEVEL_HIGH = 'H'

    LEVEL_CHOICES = [
        (LEVEL_LOW, 'low'),
        (LEVEL_MED, 'medium'),
        (LEVEL_HIGH, 'high'),
    ]
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                primary_key=True)

    level = models.CharField(max_length=1,
                             choices=LEVEL_CHOICES,
                             default='LEVEL_LOW')
    course = models.TextField(blank=True)
    status = models.CharField(max_length=1,
                              choices=[('a', 'active'), ('b', 'blocked')],
                              default='active')

    def __str__(self):
        return f"Student <{self.user}>"


class Score(models.Model):
    group = models.CharField(max_length=255,
                             blank=False)
    date = models.DateField()
    score = models.IntegerField()


class Course(models.Model):
    course_author = models.ForeignKey(Teacher,
                                      on_delete=models.CASCADE,
                                      default=None)
    name = models.TextField(default='How to learn english by 24 days',
                            unique=True)


class Schedule(models.Model):
    next_lesson = models.DateField()
    next_lesson_name = models.TextField()
