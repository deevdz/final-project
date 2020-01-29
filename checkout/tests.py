from django.test import TestCase
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.test.client import Client
from allauth.utils import get_user_model
from .models import Order, Address

# Tests for Cart Models.
class TestCartModel(TestCase):

    def test_can_create_an_address(self):
        address = Address(full_name = 'Test Name', phone_number = '1234',
                                      address_line_1 = 'Test Address',
                                      address_line_2 = 'Test Address 2',
                                      town = 'Town', county = 'County',
                                      postcode = 'TEST123',
                                      user_id=1)
        user = get_user_model().objects.create(username='testuser')
        address.save()
        self.assertEqual(address.full_name, 'Test Name')
        self.assertEqual(address.phone_number, '1234')
        self.assertEqual(address.address_line_1, 'Test Address')
        self.assertEqual(address.address_line_2, 'Test Address 2')
        self.assertEqual(address.town, 'Town')
        self.assertEqual(address.county, 'County')
        self.assertEqual(address.postcode, 'TEST123')
        self.assertEqual(address.user_id, 1)


# Tests for Cart Views.
class TestCheckoutViews(TestCase):

    def test_checkout_page(self):
        self.user = get_user_model().objects.create_user(
            'test', 'test@test.com', 'password')
        page = self.client.get('/accounts/login/?next=/checkout/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'account/login.html')
