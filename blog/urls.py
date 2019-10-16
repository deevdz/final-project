from django.conf.urls import url, include
from .views import blog, blog_detail, search_blog, list_blog_by_category

urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^search/$', search_blog, name='search_blog'),
    url(r'^category/(?P<slug>[-\w]+)/$', list_blog_by_category, name='list_blog_by_category'),
    url(r'^(?P<slug>[-\w]+)/$', blog_detail, name='blog_detail'),
]