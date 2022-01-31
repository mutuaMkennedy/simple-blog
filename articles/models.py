from django.db import models
from django.conf import settings

# TO DO: Add cloudinary CDN to handle media files
class Article(models.Model):
    title = models.CharField(max_length=125)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    # ADD THUMBNAIL
    thumb = models.ImageField(default='default.png', blank=True)
    # ADD AUTHOR
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + '...'







