from django.conf.urls import url, include
from .views import blog, blog_detail, search_blog, list_blog_by_category, blog_create, blog_update, blog_delete

urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^search/$', search_blog, name='search_blog'),
    url(r'^category/(?P<slug>[-\w]+)/$', list_blog_by_category, name='list_blog_by_category'),
    url(r'^create/$', blog_create, name='blog_create'),
    url(r'^(?P<slug>[-\w]+)/$', blog_detail, name='blog_detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', blog_update, name='blog_update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', blog_delete, name='blog_delete'),    
]