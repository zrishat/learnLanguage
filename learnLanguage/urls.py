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
from english import views
from learnLanguage import settings
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from graphene_django.views import GraphQLView

drf = routers.DefaultRouter()
drf.register(r'users', views.UserViewSet)
drf.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', views.CourseListView.as_view(), name='homepage'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='detail_course'),
    path('add_course/', views.CourseCreateView.as_view(), name='add_course'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(),
         name='delete_course'),
    path('courses/<int:pk>/update/', views.CourseUpdateView.as_view(), name='edit_course'),

    path('courses/', views.CourseListView.as_view()),
    path('admin/', admin.site.urls),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token),
    path('drf/', include(drf.urls)),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('frontend/', views.FrontendView.as_view(), name='frontend')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls)),
    )
