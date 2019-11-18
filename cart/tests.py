from django.test import TestCase
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.test.client import Client
from allauth.utils import get_user_model
from .models import OrderLineItem

# Create your tests here.

class TestCartModel(TestCase):

    def test_can_create_a_order_line_item(self):
        orderlineitem = OrderLineItem(item_id =1, quantity=2, purchased=False,  user_id=1)
        user = get_user_model().objects.create(username='testuser')
        orderlineitem.save()
        self.assertEqual(orderlineitem.item_id, 1)
        self.assertEqual(orderlineitem.quantity, 2)
        self.assertEqual(orderlineitem.purchased, False)
        self.assertEqual(orderlineitem.user_id, 1)
    