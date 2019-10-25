from django.test import TestCase
from django.test.client import Client
from django.shortcuts import render, get_object_or_404, redirect, reverse
from allauth.utils import get_user_model
from .models import HomepageSlider

class TestHomeModel(TestCase):

    def test_can_create_a_homepage_slide(self):
        slide = HomepageSlider(title='Create a Test Slide', subtitle='Slide Subtitle', status='draft', user_id=1)
        user = get_user_model().objects.create(username='testuser')
        slide.save()
        self.assertEqual(slide.title, 'Create a Test Slide')
        self.assertEqual(slide.subtitle, 'Slide Subtitle')
        self.assertEqual(slide.status, 'draft')
        self.assertEqual(slide.user_id, 1)

class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_get_about_page(self):
        page = self.client.get("/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html") 