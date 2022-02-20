import graphene
from graphene_django import DjangoObjectType

from english.models import MyUser, Teacher, Student, Course


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = "__all__"


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher
        fields = "__all__"


class MyUserType(DjangoObjectType):
    class Meta:
        model = MyUser
        fields = "__all__"


class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)
    all_teachers = graphene.List(TeacherType)
    all_users = graphene.List(MyUserType)
    all_course = graphene.List(CourseType)

    def resolve_all_students(self, root):
        return Student.objects.all()

    def resolve_all_teachers(self, root):
        return Teacher.objects.all()

    def resolve_all_users(self, root):
        return MyUser.objects.all()

    def resolve_all_course(self, root):
        return Course.objects.all()


schema = graphene.Schema(query=Query)
