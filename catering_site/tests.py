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

    def test_about(self):
        c = Client()
        response = c.get("/about")
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        c = Client()
        response = c.get("/contact")
        self.assertEqual(response.status_code, 200)

    def test_menus(self):
        c = Client()
        response = c.get("/menus")
        self.assertEqual(response.status_code, 200)
