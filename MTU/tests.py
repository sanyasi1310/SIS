from django.test import TestCase


from django.test import SimpleTestCase
from django.urls import reverse, resolve
from MTU.views import masterpage, Home, faculty, campus, about


class TestUrls(SimpleTestCase):

    def test_Home_url_is_resolved(self):
        url = reverse('Home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, Home)


    def test_masterpage_url_is_resolved(self):
        url = reverse('masterpage')
        print(resolve(url))
        self.assertEquals(resolve(url).func, masterpage )

    def test_faculty_url_is_resolved(self):
            url = reverse('faculty')
            print(resolve(url))
            self.assertEquals(resolve(url).func, faculty)

    def test_campus_url_is_resolved(self):
            url = reverse('campus')
            print(resolve(url))
            self.assertEquals(resolve(url).func, campus)

    def test_about_url_is_resolved(self):
            url = reverse('about')
            print(resolve(url))
            self.assertEquals(resolve(url).func, about)
# Create your tests here.
