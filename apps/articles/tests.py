from django.test import TestCase
from django.urls import reverse
from .models import Article, SportCategory
from django.utils import timezone

class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a SportCategory instance
        SportCategory.objects.create(name='Test Category')
        # Create an Article instance with the created SportCategory
        Article.objects.create(article_title='Test Article', article_text='Test Text', pub_date='2024-05-27', category=SportCategory.objects.get(id=1))

    def test_article_content(self):
        # Retrieve the Article instance
        article = Article.objects.get(id=1)
        # Define expected values for article fields
        expected_article_title = f'{article.article_title}'
        expected_article_text = f'{article.article_text}'
        expected_category = f'{article.category}'

        # Assert that the retrieved values match the expected values
        self.assertEqual(expected_article_title, 'Test Article')
        self.assertEqual(expected_article_text, 'Test Text')
        self.assertEqual(expected_category, 'Test Category')


class ArticleViewTests(TestCase):

    def setUp(self):
        # Create a SportCategory instance
        self.category = SportCategory.objects.create(name="Test Category")
        # Create an Article instance with the created SportCategory
        self.article = Article.objects.create(
            article_title="Test Article",
            article_text="Text",
            pub_date=timezone.now(),
            category=self.category
        )

    def test_index_view(self):
        # Make a GET request to the index view
        response = self.client.get(reverse('articles:index'))
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains the article title
        self.assertContains(response, "Test Article")
