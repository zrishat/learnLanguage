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
    context_object_name = 'courses'
    template_name = 'course/course_list.html'


class CourseDetailView(PageTitleMixin, DetailView):
    model = Course
    page_title = 'Course Detail'
    template_name = 'course/course_detail.html'

    def get(self, request, course_pk):
        course = get_object_or_404(Course, pk=course_pk)

        context = {
            'course': course
        }
        return render(request, 'course/course_detail.html', context)


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


# Example FBV
def course_list(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'course/course_list.html', context=context)
