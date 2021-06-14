from django.test import TestCase
from django.urls.base import resolve
from rest_framework.reverse import reverse
from neobis_app.views import Course_list, Course_detail
from django.urls import reverse
from neobis_app.serializers import CourseSerializer
from neobis_app.models import Category, Course


class TestViews(TestCase):
    def setUp(self):
        category = Category.objects.create(id=2, name='Geogre', imgpath=None)
        Course.objects.create(
            id=2, name='Test', description='Test course', category=category, logo=None)

    def test_course_list(self):
        response = self.client.get(reverse('courses_list_api'))
        self.assertEquals(response.status_code, 200)

    def test_course_list_data(self):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        response = self.client.get(reverse('courses_list_api'))
        self.assertEquals(response.data, serializer.data)

    def test_course_list_2(self):
        url = reverse('courses_list_api')
        self.assertEquals(resolve(url).func.view_class, Course_list)

    def test_course_detail(self):
        url = reverse('courses_detail_api', args=[1])
        self.assertEquals(resolve(url).func.view_class, Course_detail)
