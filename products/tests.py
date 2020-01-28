from django.test import TestCase
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime
from .models import Product, Workshop


# Testing Product Models here
class TestProductModel(TestCase):

    def test_can_create_a_product(self):
        product = Product(product_type='voucher',
                          title='Create a Test Product',
                          description='This is a test product',
                          status='DRAFT', price=25.00, user_id=1)
        user = get_user_model().objects.create(username='testuser')
        product.save()
        self.assertEqual(product.product_type, 'voucher')
        self.assertEqual(product.title, 'Create a Test Product')
        self.assertEqual(product.description, 'This is a test product')
        self.assertEqual(product.status, 'DRAFT')
        self.assertEqual(product.price, 25.00)
        self.assertEqual(product.user_id, 1)

    def test_can_create_a_product_workshop(self):
        user = get_user_model().objects.create(username='testuser')
        workshop = Workshop(product_type='workshop',
                            title='Create a Test Product',
                            description='This is a test product',
                            status='DRAFT',
                            price=25.00, user_id=1,
                            workshop_location='headford',
                            workshop_start_date=datetime.now(),
                            workshop_start_time=datetime.now(),
                            workshop_end_time=datetime.now(),)
        workshop.save()
        self.assertEqual(workshop.product_type, 'workshop')
        self.assertEqual(workshop.title, 'Create a Test Product')
        self.assertEqual(workshop.description, 'This is a test product')
        self.assertEqual(workshop.status, 'DRAFT')
        self.assertEqual(workshop.price, 25.00)
        self.assertEqual(workshop.user_id, 1)
        self.assertEqual(workshop.workshop_location, 'headford')


# Testing Product Views here
class TestProductViews(TestCase):

    def test_get_product_page(self):
        page = self.client.get('/workshops/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'workshops.html')
