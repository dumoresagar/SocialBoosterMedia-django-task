from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Item

class ItemAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Item.objects.create(name="A", description="first", value=10)
        Item.objects.create(name="B", description="second", value=60)

    def test_list_items(self):
        res = self.client.get(reverse('item-list-create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(len(res.data) >= 2)

    def test_create_item(self):
        payload = {"name":"C","description":"third","value":5}
        res = self.client.post(reverse('item-list-create'), payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Item.objects.filter(name="C").exists())
