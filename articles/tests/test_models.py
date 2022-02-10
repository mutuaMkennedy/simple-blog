from django.test import TestCase
from django.template.defaultfilters import slugify
from articles import models

class ModelsTestCase(TestCase):
    def setUp(self):
        """create an article"""
        self.article = models.Article.objects.create(
                        path="1",
                        depth=1,
                        title='a test blog',
                        body="This is a test blog"
                        )
    
    def test_article_has_slug(self):
        """check if a slug has been generated for our created article"""
        self.assertEqual(self.article.slug, slugify(self.article.title))
