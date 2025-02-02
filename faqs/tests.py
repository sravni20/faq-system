from django.test import TestCase
from rest_framework.test import APITestCase
from .models import FAQ
from django.urls import reverse

# Create your tests here.

class FAQModelTests(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework."
        )

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a web framework.")

    def test_translation_fields_created(self):
        self.assertIsNotNone(self.faq.question_hi)
        self.assertIsNotNone(self.faq.question_bn)
        self.assertIsNotNone(self.faq.answer_hi)
        self.assertIsNotNone(self.faq.answer_bn)

    def test_str_method(self):
        self.assertEqual(str(self.faq), "What is Django?")

class FAQAPITests(APITestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Python?",
            answer="Python is a programming language."
        )
        self.url = reverse('faq-list')

    def test_get_faqs_english(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], "What is Python?")

    def test_get_faqs_hindi(self):
        response = self.client.get(f"{self.url}?lang=hi")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data[0]['question'])
        self.assertNotEqual(response.data[0]['question'], "What is Python?")

    def test_get_faqs_bengali(self):
        response = self.client.get(f"{self.url}?lang=bn")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data[0]['question'])
        self.assertNotEqual(response.data[0]['question'], "What is Python?")
