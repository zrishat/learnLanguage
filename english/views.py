from django.contrib.auth.models import Group, User
from rest_framework import viewsets, permissions

from .serializers import UserSerializer, GroupSerializer
from .tasks import send_mail_client, send_mail_company
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, FormView

from english.forms import ContactForm
from english.models import Course, MyUser


class PageTitleMixin:
    page_title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = self.page_title
        return context


class CourseListView(PageTitleMixin, ListView):
    model = Course
    page_title = 'Course List'
    template_name = 'course/course_list.html'

    def get_queryset(self):
        return super().get_queryset().select_related('course_author__user')


class ContactView(PageTitleMixin, ListView, FormView):
    model = MyUser
    page_title = 'Contacts List'
    template_name = 'course/contacts_list.html'
    fields = '__all__'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        subject = 'Test message from test website'
        text = form.cleaned_data['message']
        email = form.cleaned_data['email']
        task = send_mail_client.delay(text, email)
        print('Task client.id: ', task.id)
        task = send_mail_company.delay(text, email)
        print('Task company.id: ', task.id)
        return super().form_valid(form)


class CourseDetailView(PageTitleMixin, DetailView):
    model = Course
    page_title = 'Course Detail'
    template_name = 'course/course_detail.html'

    def get_queryset(self):
        return super().get_queryset().select_related('course_author__user')


class CourseDeleteView(PageTitleMixin, DeleteView):
    model = Course
    page_title = 'Course Delete'
    success_url = reverse_lazy('homepage')
    template_name = 'course/course_confirm_delete.html'


class CourseUpdateView(PageTitleMixin, UpdateView):
    model = Course
    page_title = 'Course Update'
    fields = ['name']
    success_url = reverse_lazy('homepage')
    template_name = 'course/course_form.html'


class CourseCreateView(PageTitleMixin, CreateView):
    model = Course
    page_title = 'Course Add'
    success_url = reverse_lazy('homepage')
    fields = '__all__'
    template_name = 'course/course_form.html'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]