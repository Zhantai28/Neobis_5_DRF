from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('courses/', views.Course_list.as_view(), name='courses_list_api'),
    path('courses/<int:pk>/', views.Course_detail.as_view(),
         name='courses_detail_api')
]


urlpatterns = format_suffix_patterns(urlpatterns)
