from django.db import models
from django.conf import settings
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


# TO DO: Add cloudinary CDN to handle media files
class Article(Page):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # ADD THUMBNAIL
    thumb = models.ImageField(default='default.png', blank=True)
    # ADD AUTHOR
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + '...'







