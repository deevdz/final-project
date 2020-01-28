from django.test import TestCase
from django.test.client import Client
from django.shortcuts import render, get_object_or_404, redirect, reverse
from allauth.utils import get_user_model
from .models import HomepageSlider


# Testing the Home App Models
class TestHomeModel(TestCase):

    def test_can_create_a_homepage_slide(self):
        slide = HomepageSlider(title='Create a Test Slide',
                               subtitle='Slide Subtitle',
                               status='draft', user_id=1)
        user = get_user_model().objects.create(username='testuser')
        slide.save()
        self.assertEqual(slide.title, 'Create a Test Slide')
        self.assertEqual(slide.subtitle, 'Slide Subtitle')
        self.assertEqual(slide.status, 'draft')
        self.assertEqual(slide.user_id, 1)


# Testing the Home App Views
class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_get_about_page(self):
        page = self.client.get("/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")

    def test_get_timetable_page(self):
        page = self.client.get("/timetable/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "timetable.html")

    def test_get_hot_yoga_page(self):
        page = self.client.get("/bikram-hot-yoga/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bikram-hot-yoga.html")

    def test_get_meditation_page(self):
        page = self.client.get("/meditation/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "meditation.html")

    def test_get_pregnancy_yoga_page(self):
        page = self.client.get("/pregnancy-yoga/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "pregnancy-yoga.html")

    def test_get_reformer_bed_page(self):
        page = self.client.get("/reformer-bed/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "reformer-bed.html")

    def test_get_total_barre_page(self):
        page = self.client.get("/total-barre/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "total-barre.html")

    def test_get_what_do_i_need_page(self):
        page = self.client.get("/what-do-i-need/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "what-do-i-need.html")

    def test_get_yogalates_page(self):
        page = self.client.get("/yogalates/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "yogalates.html")
