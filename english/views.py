from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from english.models import Course


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
