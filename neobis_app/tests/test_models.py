from django.test import TestCase
from neobis_app.models import Category, Course, Branch, Contact


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Bob', imgpath=None)

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 150)

    def test_image(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('imgpath').verbose_name
        self.assertEquals(field_label, 'imgpath')


class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Bob', imgpath=None)
        Course.objects.create(
            name='Neobis', description='Neobis courses', category=category, logo=None)

    def test_name_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('name').max_length
        self.assertEquals(max_length, 80)

    def test_description_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_description_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('description').max_length
        self.assertEquals(max_length, 1000)

    def test_foreignKey_label(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

    def test_image(self):
        course = Course.objects.get(id=1)
        field_label = course._meta.get_field('logo').verbose_name
        self.assertEquals(field_label, 'logo')


class BranchModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(id=2, name='Geogre', imgpath=None)
        course = Course.objects.create(
            id=2, name='Test', description='Test course', category=category, logo=None)

        Branch.objects.create(
            latitude='This is a test', longitude='Second test', address='Adress test', course=course)

    def test_latitude_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('latitude').verbose_name
        self.assertEquals(field_label, 'latitude')

    def test_latitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('latitude').max_length
        self.assertEquals(max_length, 250)

    def test_longitude_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('longitude').verbose_name
        self.assertEquals(field_label, 'longitude')

    def test_longitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('longitude').max_length
        self.assertEquals(max_length, 250)

    def test_address_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')

    def test_address_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('address').max_length
        self.assertEquals(max_length, 250)

    def test_foreignKey_label(self):
        branch = Branch.objects.get(id=1)
        field_label = branch._meta.get_field('course').verbose_name
        self.assertEquals(field_label, 'course')


class ContactModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(id=3, name='Geogre', imgpath=None)
        course = Course.objects.create(
            id=3, name='Test', description='Test course', category=category, logo=None)

        Contact.objects.create(type=2, value='Test value', course=course)

    def test_type(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'type')

    def test_value_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('value').verbose_name
        self.assertEquals(field_label, 'value')

    def test_value_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('value').max_length
        self.assertEquals(max_length, 300)

    def test_foreignKey_label(self):
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('course').verbose_name
        self.assertEquals(field_label, 'course')
