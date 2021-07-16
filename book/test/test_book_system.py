import json
from django.test import TestCase
from django.urls import reverse
from book.test_factory import BookFactory
from rest_framework.test import APIClient
from rest_framework import status


class TestBookSystem(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.api_client = APIClient()

    def test_user_is_able_to_add_book(self):
        """
        Testing post api call Which is used to create book in local database
        """
        post_data = {"name": "My First Updated Book1",
                     "isbn": "123-3213243567",
                     "authors": ["John Doe"],
                     "number_of_pages": 350,
                     "publisher": "Acme Books Publishing",
                     "country": "United States",
                     "release_date": "2019-01-01"
                     }
        response = self.api_client.post(reverse('books-list'), json.dumps(post_data),
                                        content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_is_able_to_get_books(self):
        """
        Testing user is able to get list of book instance
        """
        book = BookFactory(authors=['a'])
        response = self.api_client.get(reverse('books-list'), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_is_able_to_get_book_by_id(self):
        """
        Testing user is able to get a book instance using book id
        """
        book = BookFactory(authors=['a'])
        response = self.api_client.get(reverse('books-detail', kwargs={'pk': book.id}), content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_is_able_to_update_books(self):
        """
        Testing user is able to partial update a book detail using book id
        """
        book = BookFactory(authors=['a'])
        patch_data = {
            "authors": ['a', 'b']
        }
        response = self.api_client.patch(reverse('books-detail', kwargs={'pk': book.id}),
                                         json.dumps(patch_data),
                                         content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_is_able_to_delete_book(self):
        """
        Testing user is able to delete using book id
        """
        book = BookFactory(authors=['a'])
        response = self.api_client.delete(reverse('books-detail', kwargs={'pk': book.id}),
                                          content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_external_api(self):
        """
        Testing user is able get data from ice and fire api
        """
        response = self.api_client.get(reverse('ice_and_fire'),
                                       content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
