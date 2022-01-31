from django.conf.urls import url
from . import views


app_name = 'articles'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.article_create, name='article_create'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='article_detail'),
]






















