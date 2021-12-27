"""learnLanguage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import english.views as english
from learnLanguage import settings

urlpatterns = [
    path('', english.CourseListView.as_view(), name='homepage'),
    path('courses/<int:course_pk>/', english.CourseDetailView.as_view(), name='detail_course'),
    path('add_course/', english.CourseCreateView.as_view(), name='add_course'),
    path('courses/<int:pk>/delete/', english.CourseDeleteView.as_view(),
         name='delete_course'),
    path('courses/<int:pk>/update/', english.CourseUpdateView.as_view(), name='edit_course'),

    path('courses/', english.course_list),  # example FBV
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls)),
    )