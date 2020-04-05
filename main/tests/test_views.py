from django.test import TestCase
from django.urls import reverse
from main import forms

# Create your tests here.

# Our first test will check to ensure that our site is up and running and displays our homepage


class TestPage(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'MySite')

    def test_about_us_page_works(self):
        response = self.client.get(reverse("about-us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')
        self.assertContains(response, "MySite")

    def test_contact_us_page_works(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact_form.html")
        self.assertContains(response, "MySite")
        self.assertIsInstance(
            response.context["form"], forms.ContactForm
        )