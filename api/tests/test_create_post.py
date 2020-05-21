from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse


client = APIClient()

class GetAllPostsTest(APITestCase):

    def test_post_creation(self):
        
        url = reverse('get-posts')
        data = {
            'id': 7,
            'url': "/posts/7",
            'title': "New substitution rules",
            'body': "balloteelli is a foolxd",
            'created': "2020-05-15",
            'modified': "2020-05-17",
            'tags': [
                "New",
                "substitution",
                "rules"
            ],
            'userId': 8
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)

