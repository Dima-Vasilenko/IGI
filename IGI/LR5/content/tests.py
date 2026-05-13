from django.test import TestCase

from .models import News


class NewsTest(TestCase):

    def test_create_news(self):

        news = News.objects.create(
            title='Test News',
            short_description='Short',
            full_text='Full text'
        )

        self.assertEqual(
            news.title,
            'Test News'
        )

    def test_news_page(self):

        response = self.client.get('/news/')

        self.assertEqual(
            response.status_code,
            200
        )