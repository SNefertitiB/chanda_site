from django.test import TestCase
from django.test import Client

# Create your tests here.
class URLsTests(TestCase):
    def test_admin(self):
        c = Client()
        response = c.get("/admin/")
        self.assertEqual(response.status_code, 302)
    def test_home(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
