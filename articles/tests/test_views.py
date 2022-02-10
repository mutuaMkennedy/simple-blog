from django.test import TestCase
from django.template.defaultfilters import slugify
from articles import models

class ViewsTestCase(TestCase):
    def setUp(self):
        """create an article"""
        self.article = models.Article.objects.create(
                path="1",
                depth=1,
                title='a test blog',
                body="This is a test blog"
                )

    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_article_detail_loads_properly(self):
        """The detail page loads properly"""
        slug = self.article.slug
        response = self.client.get(f'/articles/{slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_detail.html')
