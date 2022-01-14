from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Snack
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

class SnackModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test',password='pass')
        test_user.save()

        test_Snack = Snack.objects.create(
            author = test_user,
            name = 'A name',
            description = 'Some random text'
        )
        test_Snack.save()

    def test_blog_content(self):
        snack = Snack.objects.get(id=1)

        self.assertEqual(str(snack.author), 'test')
        self.assertEqual(snack.name, 'A name')
        self.assertEqual(snack.description, 'Some random text')
        
class APITEST(APITestCase):
        
    def test_create(self):
        test_user = get_user_model().objects.create_user(username='test',password='pass')
        test_user.save()

        url = reverse('snack_list')
        data = {
            "name":"Testing is Fun!!!",
            "description":"when the right tools are available",
            "author":test_user.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Snack.objects.count(), 1)
        self.assertEqual(Snack.objects.get().name, data['name'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='test',password='pass')
        test_user.save()

        test_snack = Snack.objects.create(
            author = test_user,
            name = 'Snack',
            description = 'A mini meal'
        )

        test_snack.save()

        url = reverse('snack_detail',args=[test_snack.id])
        data = {
            "name":"Update Snack",
            "author":test_snack.author.id,
            "description":test_snack.description,
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Snack.objects.count(), test_snack.id)
        self.assertEqual(Snack.objects.get().name, data['name'])


    def test_delete(self):
        test_user = get_user_model().objects.create_user(username='test',password='pass')
        test_user.save()

        test_Snack = Snack.objects.create(
            author = test_user,
            name = 'Snack',
            description = 'A mini meal'
        )

        test_Snack.save()

        snack = Snack.objects.get()

        url = reverse('snack_detail', kwargs={'pk': snack.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)