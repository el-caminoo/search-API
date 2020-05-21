from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse, include, path


client = APIClient()

class GetAllPostsTest(APITestCase):

    def test_get_all_posts(self):
        url = reverse('get-posts')
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

