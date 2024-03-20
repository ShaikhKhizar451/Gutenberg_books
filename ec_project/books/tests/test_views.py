from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import BookListAPIView

class BookListViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_book_list_view(self):
        url = reverse('book-list')
        request = self.factory.get(url)
        response = BookListAPIView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        # Add more test cases to verify the behavior of your views
